# TaskWarrior GUI

A modern, intuitive Streamlit-based graphical interface for TaskWarrior that provides dynamic task management and enhanced visualization of task attributes.

## Features

- 📊 Clean, modern interface for TaskWarrior
- 🔍 Dynamic filtering by status, priority, and project
- 📈 Real-time task urgency calculation and display
- ✨ Easy task creation with priority and project assignment
- 🎯 One-click task completion
- 📱 Responsive design that works on both desktop and mobile

## Installation

1. Ensure you have TaskWarrior installed:
   ```bash
   # For Ubuntu/Debian
   sudo apt-get install taskwarrior
   
   # For macOS
   brew install task
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/tom-doerr/taskwarrior-gui.git
   cd taskwarrior-gui
   ```

3. Install Python dependencies:
   ```bash
   pip install streamlit pandas
   ```

## Usage

1. Start the Streamlit app:
   ```bash
   streamlit run main.py
   ```

2. Open your browser and navigate to the displayed URL (typically http://localhost:8501)

3. Use the sidebar to:
   - Add new tasks with descriptions, priorities, and projects
   - Filter tasks by status, priority, and project

4. In the main view:
   - See all your tasks with their urgency scores
   - Complete tasks with one click
   - View task details including projects and priorities

## Dependencies

- Python 3.8+
- TaskWarrior
- Streamlit
- Pandas

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Screenshot

[Screenshot to be added]

## Acknowledgments

- TaskWarrior team for their excellent task management tool
- Streamlit team for their amazing framework
