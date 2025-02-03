import streamlit as st
import pandas as pd
from taskwarrior import TaskWarrior
from utils import create_task_card, filter_tasks

# Initialize TaskWarrior
if 'task_warrior' not in st.session_state:
    st.session_state.task_warrior = TaskWarrior()

# Page config
st.set_page_config(
    page_title="TaskWarrior GUI",
    page_icon="✅",
    layout="wide"
)

# Title
st.title("TaskWarrior GUI")

# Sidebar - Add New Task
with st.sidebar:
    st.header("Add New Task")

    # Task input form
    with st.form("new_task_form", clear_on_submit=True):
        description = st.text_input("Description", key="description")
        priority = st.selectbox("Priority (optional)", ["", "H", "M", "L"], key="priority")
        project = st.text_input("Project (optional)", key="project")

        submitted = st.form_submit_button("Add Task")
        if submitted:
            if not description:
                st.error("Description is required!")
            else:
                with st.spinner("Adding task..."):
                    try:
                        st.session_state.task_warrior.add_task(
                            description,
                            priority if priority else None,
                            project if project else None
                        )
                        st.success("Task added successfully!")
                        # Clear the form fields
                        st.session_state.description = ""
                        st.session_state.priority = ""
                        st.session_state.project = ""
                    except Exception as e:
                        st.error(f"Error adding task: {str(e)}")

# Main content
# Filters
col1, col2, col3 = st.columns(3)

with col1:
    status_filter = st.selectbox("Status", ["All", "Pending", "Completed"])
with col2:
    priority_filter = st.selectbox("Priority", ["All", "H", "M", "L", "None"])
with col3:
    # Get unique projects
    try:
        tasks_df = st.session_state.task_warrior.get_tasks()
        if not tasks_df.empty:
            projects = ["All"] + sorted([p for p in tasks_df['project'].unique() if p and p != "None"]) + ["None"]
        else:
            projects = ["All", "None"]
        project_filter = st.selectbox("Project", projects)
    except Exception as e:
        st.error(f"Error loading projects: {str(e)}")
        project_filter = "All"

# Get and filter tasks
try:
    tasks_df = st.session_state.task_warrior.get_tasks()
    filtered_df = filter_tasks(tasks_df, status_filter, priority_filter, project_filter)

    if filtered_df.empty:
        st.info("No tasks found matching the current filters.")
    else:
        # Display tasks
        for _, task in filtered_df.iterrows():
            create_task_card(task)
            st.divider()

except Exception as e:
    st.error(f"Error loading tasks: {str(e)}")

# Footer
st.markdown("---")
st.markdown("TaskWarrior GUI - Manage your tasks with ease")