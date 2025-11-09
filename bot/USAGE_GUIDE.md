# Complete Usage Guide - AI Tech Stack Advisor

## Table of Contents
1. [Installation](#installation)
2. [Running the Agent](#running-the-agent)
3. [Understanding the Questions](#understanding-the-questions)
4. [Interpreting Recommendations](#interpreting-recommendations)
5. [Using the Generated Prompts](#using-the-generated-prompts)
6. [Managing Your Kanban Board](#managing-your-kanban-board)
7. [Advanced Usage](#advanced-usage)
8. [Tips & Best Practices](#tips--best-practices)

---

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

```bash
# 1. Navigate to the project directory
cd /Users/mahekparvez/Desktop/Prin/prenup

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Test with demo
python3 bot/demo.py
```

---

## Running the Agent

### Method 1: Shell Script (Easiest)

```bash
./bot/run_agent.sh
```

### Method 2: Direct Python

```bash
python3 bot/tech_stack_agent.py
```

### Method 3: Demo Mode (No Input Required)

```bash
python3 bot/demo.py
```

---

## Understanding the Questions

### Question 1: Platform & Timeline

**What it's asking:**
- What platform(s) do you need? (web, mobile, desktop)
- MVP or production-ready?
- How long until launch?

**Good answers:**
```
✅ "Web application, MVP for testing, 2-3 months timeline"
✅ "Mobile app for iOS and Android, production-ready, 6 months"
✅ "Desktop app for Mac, need it quick for demo in 3 weeks"
```

**Bad answers:**
```
❌ "Yes"
❌ "App"
❌ "Soon"
```

**Keywords the agent looks for:**
- Platform: web, mobile, iOS, Android, desktop, browser
- Stage: MVP, prototype, production, enterprise
- Timeline: weeks, months, year, quick, urgent

---

### Question 2: Team & Resources

**What it's asking:**
- Team's technical skill level?
- Any existing infrastructure to integrate?
- Budget for development and hosting?

**Good answers:**
```
✅ "Intermediate JavaScript team, no existing infra, $500/month budget"
✅ "Beginner, learning React, free/low-cost only, side project"
✅ "Advanced team, need to integrate with existing Django API, unlimited budget"
```

**Bad answers:**
```
❌ "Good"
❌ "Some money"
❌ "Engineers"
```

**Keywords the agent looks for:**
- Experience: beginner, intermediate, advanced, expert, learning
- Infrastructure: existing, integrate, legacy, current system
- Budget: low, cheap, free, medium, high, enterprise, unlimited

---

### Question 3: Features & Scale

**What it's asking:**
- What features do you need?
- How many users?
- Special requirements?

**Good answers:**
```
✅ "Real-time chat, file uploads, notifications, expect 1000 users initially"
✅ "Drag-and-drop interface, offline mode, data visualization, 10k users"
✅ "Basic CRUD, authentication, 100 users, simple analytics"
```

**Bad answers:**
```
❌ "Everything"
❌ "Many features"
❌ "Lots of users"
```

**Keywords the agent looks for:**
- Features: real-time, offline, file upload, notifications, auth, analytics, collaboration
- Scale: small, 100, 1000, 10k, large, millions
- Special: visualization, dashboard, integration

---

## Interpreting Recommendations

### Priority Levels

#### 🔴 ESSENTIAL (Must Have)
These are critical for your project. Start here.

**Example:**
```
Frontend > Core Languages
Tools: HTML5, CSS3, JavaScript
Why: Essential for web development
```

**Action:** Implement these first. Use the setup prompts provided.

---

#### 🟡 RECOMMENDED (Should Have)
Important for quality and scalability, but not blocking.

**Example:**
```
State Management > Zustand, React Query
Why: Efficient state management for complex applications
```

**Action:** Implement after essentials are working. These improve your app significantly.

---

#### 🟢 OPTIONAL (Nice to Have)
Enhances the project but can be added later.

**Example:**
```
Testing > E2E Testing
Tools: Playwright, Cypress
Why: End-to-end testing for critical flows
```

**Action:** Add these as your project matures. Great for production apps.

---

### Tool Selection Within Categories

When multiple tools are recommended, choose based on:

1. **Your Experience**
   - Beginner: Pick the most popular (largest community)
   - Intermediate: Pick what aligns with your stack
   - Advanced: Pick what fits your specific needs

2. **Your Timeline**
   - Short: Pick tools with quick setup (Firebase, Supabase)
   - Medium: Pick balanced options (PostgreSQL, Express)
   - Long: Pick enterprise-grade (AWS, Kubernetes)

3. **Your Budget**
   - Low: Vercel, Railway, Supabase (generous free tiers)
   - Medium: DigitalOcean, Railway Pro
   - High: AWS, Google Cloud, Azure

**Example Decision:**

Recommendation says: "Clerk, Supabase Auth, NextAuth"

- **Choose Clerk if:** You want plug-and-play, have budget ($0.02/user)
- **Choose Supabase Auth if:** You're using Supabase for database
- **Choose NextAuth if:** You're using Next.js, want full control, free

---

## Using the Generated Prompts

### Setup Prompts

These help you initialize each technology.

**How to use:**

1. **Copy the entire prompt**
   ```
   I'm building [your project]. I need to set up [technology].
   
   Project context:
   - Platform(s): web
   - Stage: MVP
   - Timeline: medium
   ...
   ```

2. **Paste into Cursor or Claude**
   - In Cursor: Press Cmd+K (Mac) or Ctrl+K (Windows), paste
   - In Claude/ChatGPT: Start new conversation, paste

3. **Follow the AI's instructions**
   - It will give you step-by-step setup
   - Run the commands it provides
   - Ask follow-up questions if needed

4. **Verify it works**
   - The AI will provide a test example
   - Run it to confirm setup is correct

---

### Feature Development Prompts

These help you build specific features.

**How to use:**

1. **Start with highest-priority feature**
   - Real-time features first (if needed)
   - Authentication second
   - Other features third

2. **Copy the feature prompt**
   ```
   I'm implementing [feature] for my [platform] application.
   
   Requirements:
   - Platform: web
   - Scale: medium
   - Experience: intermediate
   ...
   ```

3. **Paste into your AI coding assistant**

4. **Iterate with the AI**
   - Ask for clarification
   - Request code examples
   - Ask about edge cases

---

### AI Tool Usage Prompts

These help you learn specific AI tools.

**How to use:**

1. **If new to an AI tool** (e.g., first time using v0 by Vercel)
   - Copy the AI tool prompt
   - Paste into ChatGPT or Claude
   - Learn how to use that tool effectively

2. **Example:**
   ```
   "I'm using v0 by Vercel to help build [my project].
   
   Show me:
   1. How to use v0 for UI components
   2. Best practices
   3. Example prompts I can use
   4. Common mistakes"
   ```

3. **Then use that AI tool**
   - Go to v0.dev
   - Use the techniques you learned
   - Build your UI components

---

## Managing Your Kanban Board

### Viewing Your Board

**Full view:**
```bash
python3 bot/tech_stack_agent.py
# Then select "Manage Kanban Board" at the end
# Option 1: View Full Board
```

**Quick view:**
```bash
# Open the JSON file in any text editor
cat kanban_your_project_name.json
```

**Markdown view:**
```bash
# The agent auto-generates a Markdown file
cat kanban_your_project_name_TIMESTAMP.md
```

---

### Updating Task Status

**Via Interactive Manager:**

1. Run the agent
2. Select "Manage Kanban Board"
3. Choose "3. Update Task Status"
4. Enter task ID (e.g., "T001")
5. Select new status:
   - 1 = To Do
   - 2 = In Progress
   - 3 = Done
   - 4 = Blocked

**Via Manual Edit:**

1. Open `kanban_your_project_name.json`
2. Find the task
3. Change `"status": "TODO"` to `"status": "IN_PROGRESS"` or `"DONE"`
4. Save

---

### Adding Notes to Tasks

**Why add notes?**
- Track what you tried
- Note issues/blockers
- Link to resources

**How:**

1. Interactive manager: Option 4
2. Enter task ID
3. Type your note
4. Note is timestamped automatically

**Example notes:**
```
"Tried PostgreSQL setup, ran into permission issue"
"Found great tutorial: https://..."
"Blocked waiting for API keys"
"Completed! Deployed to Vercel"
```

---

### Exporting Your Board

**To Markdown:**
```
# In interactive manager
Option 5: Export to Markdown
```

**Share with team:**
- Send the Markdown file
- They can see all tasks, priorities, and progress
- No special tools needed to view

---

## Advanced Usage

### Using the Agent Programmatically

```python
from bot.tech_stack_agent import TechStackAgent
from bot.kanban_tracker import create_kanban_from_agent

# Create agent
agent = TechStackAgent()
agent.start_session("My awesome app")

# Set answers programmatically
agent.answers = {
    'q1': 'Web, MVP, 2 months',
    'q2': 'Intermediate, no infra, medium budget',
    'q3': 'Real-time, auth, 1000 users'
}

# Analyze and recommend
agent.analyze_answers()
agent.generate_recommendations()

# Access recommendations
for rec in agent.recommendations['essential']:
    print(f"{rec['category']}: {rec['tools']}")

# Generate prompts
prompts = agent.generate_prompts()

# Create kanban
kanban = create_kanban_from_agent(agent)
```

---

### Customizing the Tech Stack Database

**Add your own tools:**

Edit `tech_stack_agent.py`, find `TECH_STACK` dictionary:

```python
TECH_STACK = {
    "Your Category": {
        "Your Subcategory": {
            "tools": ["Tool1", "Tool2"],
            "ai_tools": ["AI Tool 1", "AI Tool 2"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "intermediate"
        }
    }
}
```

---

### Integrating with Your Own AI

Replace the keyword matching with actual AI analysis:

```python
# In tech_stack_agent.py, modify analyze_answers()

def analyze_answers(self):
    # Instead of keyword matching, use OpenAI/Claude/Gemini
    
    import openai
    
    prompt = f"""
    Analyze these answers and extract:
    - platforms
    - stage (mvp or production)
    - experience_level
    - budget
    - features
    - scale
    
    Answers:
    {self.answers}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Parse response and set self.analysis
    # ...
```

---

## Tips & Best Practices

### 1. Start Small

❌ Don't try to implement everything at once  
✅ Do: Essential tools → Core features → Recommended tools → Optional tools

### 2. Use AI Assistants Effectively

**Best practices:**
- Copy prompts exactly as generated
- Provide context: "I'm at this step: ..."
- Ask for explanations: "Why did you choose X over Y?"
- Iterate: "This didn't work, here's the error: ..."

### 3. Track Everything in Kanban

**Update tasks as you go:**
- Started setup? → Move to "In Progress"
- Hit a blocker? → Mark as "Blocked", add note
- Finished? → Mark as "Done"

This helps you:
- See progress
- Know what's next
- Identify blockers early

### 4. Re-run for Different Phases

**MVP Phase:**
```
Answer Q1: "MVP, 2 months"
→ Get rapid development tools
```

**Production Phase:**
```
Answer Q1: "Production-ready, 6 months"
→ Get enterprise tools, testing, monitoring
```

### 5. Share with Your Team

Export everything:
```bash
# Text report for developers
tech_stack_recommendations_TIMESTAMP.txt

# JSON for programmatic use
tech_stack_export_TIMESTAMP.json

# Kanban for project managers
kanban_project_TIMESTAMP.md
```

### 6. Validate Recommendations

The agent is smart, but:
- Check if tools are actively maintained
- Read recent reviews/articles
- Consider your team's existing knowledge
- Factor in hiring (common skills vs. niche)

### 7. Budget for Learning Time

Even with AI assistants:
- New framework: +1-2 weeks
- New language: +2-4 weeks
- New paradigm (e.g., GraphQL): +1 week

Factor this into your timeline.

### 8. Start with What You Know

If the agent recommends:
- React, Vue, or Angular
- And you know React

→ Choose React, even if Vue might be "better"

**Why:** You'll move faster with familiar tools.

### 9. Use the Prompts Iteratively

**Don't just use a prompt once:**

```
Day 1: Copy setup prompt → Get basic setup
Day 2: Same prompt + "Now add [X]" → Extend it
Day 3: Same prompt + "I'm getting [error]" → Debug
```

### 10. Document Your Decisions

**In Kanban notes, record:**
- Why you chose Tool A over Tool B
- What problems you encountered
- What you'd do differently next time

This helps future you and your team.

---

## Troubleshooting

### Agent gives generic recommendations

**Problem:** Answers too vague  
**Solution:** Use specific keywords:
- ❌ "App"
- ✅ "Real-time collaborative web app"

### Too many essential tools

**Problem:** 10+ essential tools, overwhelming  
**Solution:** 
1. Start with: Frontend framework + Backend framework + Database
2. Add auth, then other features
3. Essentials can be phased

### Recommended tools I've never heard of

**Solution:**
1. Google the tool
2. Check GitHub stars/activity
3. Use AI: "Explain [Tool] vs [Alternative]"
4. If still unsure, choose the more popular option

### Kanban board won't save

**Problem:** Permission error  
**Solution:**
```bash
chmod +w .
# Or run from a directory where you have write permissions
```

### Want to modify recommendations after generation

**Solution:**
```python
# Load the JSON export
import json
with open('tech_stack_export_TIMESTAMP.json', 'r') as f:
    data = json.load(f)

# Modify
data['recommendations']['essential'].append({
    "category": "New Category",
    "subcategory": "New Tool",
    "tools": ["Tool X"],
    "reason": "My custom reason"
})

# Save
with open('tech_stack_export_modified.json', 'w') as f:
    json.dump(data, f, indent=2)
```

---

## Getting Help

1. **Check the README:** `bot/README.md`
2. **See examples:** `bot/EXAMPLE_OUTPUT.md`
3. **Run demo:** `python3 bot/demo.py`
4. **Use AI assistants:** Paste this guide + your question into Claude/ChatGPT

---

**🎉 You're ready to build!**

Remember: The agent is a starting point. Use your judgment, iterate, and don't be afraid to deviate from recommendations as you learn more about your project's specific needs.

Good luck! 🚀

