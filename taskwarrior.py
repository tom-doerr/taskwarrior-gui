import subprocess
import json
import pandas as pd
from typing import List, Dict, Optional

class TaskWarrior:
    def __init__(self):
        self.command = "task"
        # Test if task command exists
        try:
            subprocess.run([self.command, "--version"], capture_output=True, timeout=5)
        except FileNotFoundError:
            raise Exception("TaskWarrior is not installed. Please install it first.")
        except Exception as e:
            raise Exception(f"Error initializing TaskWarrior: {str(e)}")

    def _run_command(self, args: List[str]) -> str:
        try:
            result = subprocess.run(
                [self.command] + args,
                capture_output=True,
                text=True,
                check=True,
                timeout=10  # Add timeout
            )
            return result.stdout
        except subprocess.TimeoutExpired:
            raise Exception("Command timed out. Please try again.")
        except subprocess.CalledProcessError as e:
            if "No matches." in e.stderr:
                return "[]"
            raise Exception(f"TaskWarrior error: {e.stderr}")
        except Exception as e:
            raise Exception(f"Unexpected error: {str(e)}")

    def get_tasks(self, filter_str: str = "") -> pd.DataFrame:
        args = ["export"] + filter_str.split()
        output = self._run_command(args)

        if not output.strip():
            return pd.DataFrame()

        tasks = json.loads(output)
        if not tasks:
            return pd.DataFrame()

        df = pd.DataFrame(tasks)

        # Convert status to pending if not present
        if 'status' not in df.columns:
            df['status'] = 'pending'

        # Add priority if not present
        if 'priority' not in df.columns:
            df['priority'] = 'None'

        # Add project if not present
        if 'project' not in df.columns:
            df['project'] = 'None'

        return df

    def add_task(self, description: str, priority: Optional[str] = None, 
                 project: Optional[str] = None) -> None:
        if not description:
            raise ValueError("Description is required")

        args = ["add", description]
        if priority:
            args.extend(["priority:", priority])
        if project:
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