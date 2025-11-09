# 🤖 AI Tech Stack Advisor

An intelligent AI agent that analyzes your project idea, asks targeted questions, and provides personalized tech stack recommendations with custom prompts for each tool.

## Features

✨ **Smart Analysis**: Analyzes your requirements through 3 targeted questions  
🎯 **Personalized Recommendations**: Provides essential, recommended, and optional tools  
📝 **Custom Prompts**: Generates ready-to-use prompts for each recommended tool  
📋 **Kanban Tracking**: Creates a visual task board to track implementation  
🤖 **AI Tools**: Recommends 10+ AI coding assistants for each part of your stack  
💾 **Multiple Exports**: Saves to TXT, JSON, and Markdown formats  

## Quick Start

### 1. Installation

```bash
cd /Users/mahekparvez/Desktop/Prin/prenup
pip install -r requirements.txt
```

### 2. Run the Agent

```bash
python bot/tech_stack_agent.py
```

### 3. Follow the Prompts

The agent will:
1. Ask for your project idea (one line)
2. Ask 3 questions about your requirements
3. Analyze your needs
4. Generate personalized recommendations
5. Create custom prompts for each tool
6. Generate a Kanban board to track tasks

## Usage Example

```
What's your project idea? (one line): A timeline app for project management

Question 1: What platform(s) do you need this timeline app for...
Your answer: Web app, need MVP in 2 months

Question 2: What's your team's technical background...
Your answer: Intermediate level, no existing infrastructure, moderate budget

Question 3: What specific timeline features do you envision...
Your answer: Drag-and-drop, real-time collaboration, 1000 users initially
```

## Output Files

The agent generates several files:

- **`tech_stack_recommendations_[timestamp].txt`** - Full text report
- **`tech_stack_export_[timestamp].json`** - Structured JSON data
- **`kanban_[project_name].json`** - Kanban board data
- **`kanban_[project_name]_[timestamp].md`** - Kanban board in Markdown

## The 3 Questions

### Question 1: Platform & Timeline
- What platform(s)? (web, mobile, desktop)
- MVP or production-ready?
- Target timeline for launch?

### Question 2: Team & Resources
- Team's technical background?
- Existing infrastructure?
- Budget range?

### Question 3: Features & Scale
- Specific features needed?
- Expected user scale?
- Offline functionality?
- Special requirements?

## Tech Stack Database

The agent has knowledge of 100+ tools across:

- **Frontend Development**: React, Vue, Angular, Next.js, Svelte, etc.
- **Backend Development**: Node.js, Python, Go, Rust, Java, etc.
- **Databases**: PostgreSQL, MongoDB, Redis, Elasticsearch, etc.
- **DevOps**: Docker, Kubernetes, AWS, Vercel, Railway, etc.
- **Mobile**: React Native, Flutter, Swift, Kotlin, etc.
- **Testing**: Jest, Cypress, Playwright, PyTest, etc.
- **Analytics**: PostHog, Mixpanel, Tableau, Power BI, etc.

## AI Tools Recommendations

For each tech category, the agent recommends 10+ AI tools:

- **Coding Assistants**: Cursor, Windsurf, GitHub Copilot, Claude 3.5
- **Design Tools**: Figma AI, v0 by Vercel, Galileo AI, Uizard
- **Database Tools**: Text2SQL, MindsDB, DataPilot
- **DevOps Tools**: K8sGPT, Harness AI, Amazon Q
- **Testing Tools**: CodiumAI, Testim.io, Mabl

## Kanban Board Management

After generating recommendations, you can interactively manage your Kanban board:

```bash
# The agent creates tasks automatically from recommendations
# You can then:
1. View Full Board
2. View Compact Board
3. Update Task Status
4. Add Note to Task
5. Export to Markdown
6. Exit
```

### Task Statuses

- 📝 **To Do** - Not yet started
- 🔄 **In Progress** - Currently working on
- ✅ **Done** - Completed
- 🚫 **Blocked** - Blocked by dependencies

### Task Priorities

- 🔴 **High** - Essential/Critical
- 🟡 **Medium** - Recommended
- 🟢 **Low** - Optional

## Architecture

```
bot/
├── tech_stack_agent.py    # Main agent with recommendation engine
├── kanban_tracker.py       # Kanban board implementation
└── README.md              # This file
```

### `tech_stack_agent.py`

Main AI agent that:
- Asks questions and collects answers
- Analyzes requirements with keyword matching
- Generates personalized recommendations
- Creates custom prompts for each tool
- Exports to multiple formats

### `kanban_tracker.py`

Kanban board system that:
- Creates tasks from recommendations
- Tracks task status and progress
- Allows interactive management
- Exports to JSON and Markdown

## Customization

### Adding New Technologies

Edit the `TECH_STACK` dictionary in `tech_stack_agent.py`:

```python
TECH_STACK = {
    "Your Category": {
        "Your Subcategory": {
            "tools": ["Tool1", "Tool2"],
            "ai_tools": ["AI Tool 1", "AI Tool 2"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "beginner"  # or "intermediate", "advanced"
        }
    }
}
```

### Modifying Questions

Edit the `QUESTIONS` list in `tech_stack_agent.py`:

```python
QUESTIONS = [
    {
        "id": "q1",
        "question": "Your question here?",
        "keywords": {
            "category": ["keyword1", "keyword2"]
        }
    }
]
```

## Local AI Integration (Optional)

To use local AI models, uncomment one of these in `requirements.txt`:

```bash
# For Google Gemini (local)
pip install google-generativeai

# For Anthropic Claude (local)
pip install anthropic

# For Ollama (fully local)
pip install ollama
```

Then modify the agent to use your preferred AI API for enhanced recommendations.

## Examples

### Example 1: Simple Web App

**Input:** "A todo list app"  
**Platform:** Web, MVP, 1 month  
**Team:** Beginner, no infrastructure, low budget  
**Features:** Basic CRUD, 100 users  

**Recommendations:**
- Frontend: React + Tailwind CSS
- Backend: Firebase or Supabase
- Hosting: Vercel
- AI Tools: Cursor, v0 by Vercel, Claude

### Example 2: Mobile App

**Input:** "A fitness tracking app"  
**Platform:** Mobile (iOS + Android), Production, 6 months  
**Team:** Intermediate, no infrastructure, medium budget  
**Features:** Offline sync, notifications, 10k users  

**Recommendations:**
- Mobile: React Native + Expo
- Backend: Node.js + NestJS
- Database: PostgreSQL + Redis
- Cloud: AWS or Railway
- AI Tools: Cursor, Windsurf, Claude, Copilot

### Example 3: Enterprise Web App

**Input:** "A project management dashboard"  
**Platform:** Web, Production, 1 year  
**Team:** Advanced, existing infrastructure, high budget  
**Features:** Real-time collaboration, analytics, 100k users  

**Recommendations:**
- Frontend: Next.js + TypeScript + Redux
- Backend: Node.js + NestJS + GraphQL
- Database: PostgreSQL + Redis + Elasticsearch
- DevOps: Docker + Kubernetes + AWS
- Testing: Jest + Playwright + Cypress
- AI Tools: Cursor, Claude, K8sGPT, CodiumAI

## Troubleshooting

### Import Error

If you get an import error:

```bash
# Make sure you're in the correct directory
cd /Users/mahekparvez/Desktop/Prin/prenup
python bot/tech_stack_agent.py
```

### Kanban Not Saving

Check that you have write permissions in the current directory:

```bash
chmod +w .
```

### No Recommendations

Make sure your answers include relevant keywords from the questions.

## Contributing

Feel free to add more:
- Technologies to `TECH_STACK`
- Keywords to `QUESTIONS`
- Features to the recommendation engine

## License

MIT License - Feel free to use and modify!

## Author

Built for Prin (prenup project)

---

## Tips for Best Results

1. **Be Specific**: Provide detailed answers to the 3 questions
2. **Use Keywords**: Mention specific technologies you prefer
3. **Think Scale**: Be realistic about user numbers and timeline
4. **Review All**: Check essential, recommended, AND optional tools
5. **Use Prompts**: Copy the generated prompts directly into Cursor/Claude
6. **Track Progress**: Use the Kanban board to stay organized
7. **Iterate**: Run the agent again as requirements change

🚀 **Happy building!**

