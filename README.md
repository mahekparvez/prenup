# prenup

A collection of AI-powered development tools for building better projects faster.

## 🤖 New: AI Tech Stack Advisor

An intelligent agent that analyzes your project idea and provides personalized tech stack recommendations!

### Quick Start
```bash
cd /Users/mahekparvez/Desktop/Prin/prenup
./bot/run_agent.sh
```

**What it does:**
- ✨ Asks 3 targeted questions about your project
- 🎯 Recommends the best tech stack based on your needs
- 📝 Generates custom prompts for AI coding assistants (Cursor, Claude, etc.)
- 📋 Creates a Kanban board to track implementation tasks
- 🤖 Suggests 10+ AI tools for each part of your stack

**Learn more:** See [`QUICKSTART.md`](./QUICKSTART.md) and [`bot/README.md`](./bot/README.md)

---

## Development

Please cd to the directory. Then, run `pip install -r requirements.txt` to get all required dependencies at the version used for development.

## Project Structure

```
prenup/
├── bot/                      # AI Tech Stack Advisor
│   ├── tech_stack_agent.py   # Main recommendation engine
│   ├── kanban_tracker.py     # Kanban board tracker
│   ├── run_agent.sh          # Easy runner script
│   ├── README.md             # Full documentation
│   └── EXAMPLE_OUTPUT.md     # Sample output
├── tutor-prototype/          # Learning tutor prototype
├── QUICKSTART.md             # Quick start guide
└── requirements.txt          # Python dependencies
```

## Vision Board

Vision board linked [here](https://docs.google.com/document/d/1vIuQtsACtNMAWI2cJpk_HTXlcN7der7VsyV1yXhdIFk/edit?tab=t.0) (permissions required).