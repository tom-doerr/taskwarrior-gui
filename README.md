# TaskWarrior GUI

A modern, intuitive Streamlit-based graphical interface for TaskWarrior that provides dynamic task management and enhanced visualization of task attributes.

## Features

- 📊 Clean, modern interface for TaskWarrior
- 🔍 Dynamic filtering:
  - Filter by status (Pending/Completed)
  - Filter by priority (High/Medium/Low)
  - Filter by project
- 📈 Real-time task urgency calculation and display
- ✨ Task management:
  - Easy task creation with descriptions
  - Priority assignment (High/Medium/Low)
  - Project organization
  - One-click task completion
- 📱 Responsive design that works on both desktop and mobile
- 🎨 Clean and intuitive user interface with:
  - Color-coded priorities
  - Project grouping
  - Urgency scores
  - Task status indicators

## Installation

1. Ensure you have TaskWarrior installed:
   ```bash
   # For Ubuntu/Debian
   sudo apt-get install taskwarrior

   # For macOS
   brew install task

   # For other systems, visit: https://taskwarrior.org/download/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/tom-doerr/taskwarrior-gui.git
   cd taskwarrior-gui
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   # or
   pip install streamlit pandas
   ```

## Usage

1. Start the Streamlit app:
   ```bash
   streamlit run main.py
   ```

2. Open your browser and navigate to the displayed URL (typically http://localhost:5000)

3. Using the interface:
   - **Adding Tasks**: Use the sidebar form to add new tasks
   - **Task Properties**:
     - Description (required)
     - Priority (optional: High/Medium/Low)
     - Project (optional)
   - **Filtering**: Use the sidebar filters to sort and filter tasks
   - **Task Actions**: Complete tasks with one click using the action buttons

## Troubleshooting

1. **TaskWarrior Not Found**:
   - Ensure TaskWarrior is installed and accessible from command line
   - Try running `task version` to verify installation

2. **Permission Issues**:
   - Ensure TaskWarrior configuration directory exists: `~/.task/`
   - Check file permissions: `chmod -R 700 ~/.task/`

3. **Display Issues**:
   - Try clearing your browser cache
   - Ensure you're using a modern web browser

## Dependencies

- Python 3.8+
- TaskWarrior
- Streamlit
- Pandas

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

Please ensure your PR:
- Includes a clear description of the changes
- Updates documentation as needed
- Follows the existing code style
- Includes tests if applicable

## Screenshots

[Coming Soon]

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- TaskWarrior team for their excellent task management tool
- Streamlit team for their amazing framework
- All contributors who help improve this project

---
Made with ❤️ by the TaskWarrior GUI Contributors