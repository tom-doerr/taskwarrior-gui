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
    with st.form("new_task_form"):
        description = st.text_input("Description")
        priority = st.selectbox("Priority", ["None", "H", "M", "L"])
        project = st.text_input("Project")
        
        if st.form_submit_button("Add Task"):
            try:
                st.session_state.task_warrior.add_task(
                    description,
                    priority if priority != "None" else None,
                    project if project else None
                )
                st.success("Task added successfully!")
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
    tasks_df = st.session_state.task_warrior.get_tasks()
    projects = ["All"] + sorted(tasks_df['project'].unique().tolist())
    project_filter = st.selectbox("Project", projects)

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
