import streamlit as st
from typing import Dict, Any

def format_priority(priority: str) -> str:
    if not priority or priority == "None":
        return "None"
    return priority.upper()

def get_priority_color(priority: str) -> str:
    colors = {
        "H": "#FF4B4B",
        "M": "#FFA500",
        "L": "#00CC00",
        "None": "#808080"
    }
    return colors.get(priority, "#808080")

def create_task_card(task: Dict[str, Any]) -> None:
    with st.container():
        cols = st.columns([3, 1, 1, 1])
        
        # Task description
        with cols[0]:
            st.markdown(f"**{task.get('description', '')}**")
            
        # Priority
        with cols[1]:
            priority = format_priority(task.get('priority', 'None'))
            st.markdown(f"<span style='color: {get_priority_color(priority)}'>{priority}</span>",
                       unsafe_allow_html=True)
            
        # Project
        with cols[2]:
            project = task.get('project', 'None')
            st.text(project if project else 'None')
            
        # Actions
        with cols[3]:
            task_id = task.get('id')
            if task_id:
                st.button("Complete", key=f"complete_{task_id}",
                         on_click=lambda: st.session_state.task_warrior.complete_task(task_id))

def filter_tasks(df, status_filter, priority_filter, project_filter):
    if df.empty:
        return df
        
    filtered_df = df.copy()
    
    if status_filter != "All":
        filtered_df = filtered_df[filtered_df['status'] == status_filter.lower()]
        
    if priority_filter != "All":
        filtered_df = filtered_df[filtered_df['priority'] == priority_filter]
        
    if project_filter != "All":
        filtered_df = filtered_df[filtered_df['project'] == project_filter]
        
    return filtered_df
