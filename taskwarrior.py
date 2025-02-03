import subprocess
import json
import pandas as pd
import os
from typing import List, Dict, Optional

class TaskWarrior:
    def __init__(self):
        self.command = "task"
        # Test if task command exists and initialize if needed
        try:
            # First check if task exists
            result = subprocess.run([self.command, "--version"], 
                                  capture_output=True, 
                                  text=True,
                                  timeout=30)
            if result.returncode != 0:
                raise Exception("TaskWarrior not properly installed")

            # Initialize config if needed
            home = os.path.expanduser("~")
            taskrc = os.path.join(home, ".taskrc")
            if not os.path.exists(taskrc):
                # Create empty taskrc file
                with open(taskrc, 'w') as f:
                    f.write("# TaskWarrior config file\n")

                # Run task version to trigger first-time setup
                subprocess.run([self.command, "version"], 
                             capture_output=True,
                             timeout=30)

        except FileNotFoundError:
            raise Exception("TaskWarrior is not installed. Please install it first.")
        except subprocess.TimeoutExpired:
            raise Exception("TaskWarrior initialization timed out. Please try again.")
        except Exception as e:
            raise Exception(f"Error initializing TaskWarrior: {str(e)}")

    def _run_command(self, args: List[str], timeout: int = 30) -> str:
        try:
            result = subprocess.run(
                [self.command] + args,
                capture_output=True,
                text=True,
                check=True,
                timeout=timeout  # Default 30 second timeout
            )
            return result.stdout
        except subprocess.TimeoutExpired:
            if "export" in args:
                # Return empty list for export timeouts
                return "[]"
            raise Exception("Command timed out. Please try again.")
        except subprocess.CalledProcessError as e:
            if "No matches." in e.stderr:
                return "[]"
            raise Exception(f"TaskWarrior error: {e.stderr}")
        except Exception as e:
            raise Exception(f"Unexpected error: {str(e)}")

    def get_tasks(self, filter_str: str = "") -> pd.DataFrame:
        try:
            # First calculate urgency for all tasks
            self._run_command(["rc.urgency.user.tag.next.coefficient=0", "stats"])

            # Use export with proper configuration to get all attributes including urgency
            args = [
                "export",
                "rc.json.array=on",
                "rc.verbose=label",
                "rc.debug=1"
            ] + filter_str.split()

            output = self._run_command(args, timeout=60)  # Longer timeout for export

            if not output.strip():
                return pd.DataFrame({
                    'status': [],
                    'priority': [],
                    'project': [],
                    'description': [],
                    'id': [],
                    'urgency': []
                })

            tasks = json.loads(output)
            if not tasks:
                return pd.DataFrame({
                    'status': [],
                    'priority': [],
                    'project': [],
                    'description': [],
                    'id': [],
                    'urgency': []
                })

            df = pd.DataFrame(tasks)

            # Ensure required columns exist
            required_columns = {
                'status': 'pending',
                'priority': 'None',
                'project': 'None',
                'description': '',
                'id': None,
                'urgency': 0.0
            }

            for col, default in required_columns.items():
                if col not in df.columns:
                    df[col] = default

            # Convert urgency to float and ensure it's not NaN
            if 'urgency' in df.columns:
                df['urgency'] = pd.to_numeric(df['urgency'], errors='coerce').fillna(0.0)

            return df
        except Exception as e:
            print(f"Error in get_tasks: {str(e)}")
            return pd.DataFrame({
                'status': [],
                'priority': [],
                'project': [],
                'description': [],
                'id': [],
                'urgency': []
            })

    def add_task(self, description: str, priority: Optional[str] = None, 
                 project: Optional[str] = None) -> None:
        if not description:
            raise ValueError("Description is required")

        args = ["add", description]
        if priority and priority.strip():  # Only add if priority is not empty
            args.extend(["priority:", priority])
        if project and project.strip():  # Only add if project is not empty
            args.extend(["project:", project])
        self._run_command(args)

    def complete_task(self, task_id: int) -> None:
        if not task_id:
            raise ValueError("Task ID is required")
        self._run_command([str(task_id), "done"])

    def delete_task(self, task_id: int) -> None:
        if not task_id:
            raise ValueError("Task ID is required")
        self._run_command([str(task_id), "delete"])

    def modify_task(self, task_id: int, description: Optional[str] = None,
                    priority: Optional[str] = None, project: Optional[str] = None) -> None:
        if not task_id:
            raise ValueError("Task ID is required")

        args = [str(task_id), "modify"]
        if description:
            args.append(description)
        if priority:
            args.extend(["priority:", priority])
        if project:
            args.extend(["project:", project])
        self._run_command(args)