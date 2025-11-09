# 🚀 Quick Start Guide - AI Tech Stack Advisor

Get personalized tech stack recommendations in 5 minutes!

## Option 1: Using Shell Script (Recommended)

```bash
cd /Users/mahekparvez/Desktop/Prin/prenup
./bot/run_agent.sh
```

## Option 2: Direct Python

```bash
cd /Users/mahekparvez/Desktop/Prin/prenup
python3 bot/tech_stack_agent.py
```

## What You'll Get

1. **Personalized Tech Stack Recommendations**
   - Essential tools (must have)
   - Recommended tools (should have)
   - Optional tools (nice to have)

2. **Custom AI Prompts**
   - Setup prompts for each technology
   - Feature implementation prompts
   - AI tool usage prompts

3. **Kanban Board**
   - Visual task tracking
   - Automatic task creation from recommendations
   - Interactive management

4. **Multiple Export Formats**
   - Text report (.txt)
   - JSON data (.json)
   - Markdown kanban (.md)

## Example Session

```
What's your project idea? (one line): 
> A timeline app for project management

Question 1: What platform(s) do you need this timeline app for...
> Web app, MVP, need it in 2 months

Question 2: What's your team's technical background...
> Intermediate level, no existing infrastructure, moderate budget

Question 3: What specific timeline features do you envision...
> Drag-and-drop editing, real-time collaboration, expect 1000 users
```

## Tips for Best Results

✅ **Be Specific**: Mention exact platforms (web/mobile/desktop)  
✅ **State Experience Level**: Beginner, intermediate, or advanced  
✅ **Include Timeline**: Weeks, months, or year  
✅ **List Features**: Real-time, offline, notifications, etc.  
✅ **Mention Scale**: 10, 100, 1000, 10k+ users  

## Sample Output Structure

```
📊 REQUIREMENTS ANALYSIS
- Platform: Web
- Stage: MVP
- Timeline: Medium (2 months)
- Experience: Intermediate
- Budget: Medium
- Features: Drag-and-drop, Real-time collaboration

🎯 TECH STACK RECOMMENDATIONS

🔴 ESSENTIAL
  Frontend > Core Languages: HTML5, CSS3, JavaScript
  Frontend > Frontend Frameworks: React, Next.js
  Backend > Core Languages: Node.js, Python
  Database > SQL: PostgreSQL

🟡 RECOMMENDED
  State Management: Zustand, React Query
  Authentication: Clerk, Supabase Auth
  Real-time: WebSockets, GraphQL

🤖 AI TOOLS
  - Cursor (General Coding)
  - Claude 3.5 (Problem Solving)
  - v0 by Vercel (UI Design)
  - GitHub Copilot (Coding)
  
📝 CUSTOM PROMPTS
  [15+ ready-to-use prompts for each tool]

📋 KANBAN BOARD
  [Automatic task breakdown with priorities]
```

## Next Steps After Running

1. **Read the Text Report**
   - Review all recommendations
   - Note the reasoning for each tool

2. **Copy AI Prompts**
   - Use them in Cursor, Claude, or ChatGPT
   - Start with setup prompts first

3. **Check Kanban Board**
   - See all tasks laid out
   - Start with high-priority items

4. **Export for Team**
   - Share the JSON with developers
   - Share the Markdown with project managers

## Managing Your Kanban Board

After the agent runs, you can manage tasks:

```
1. View Full Board
2. View Compact Board
3. Update Task Status (Todo → In Progress → Done)
4. Add Notes to Tasks
5. Export to Markdown
6. Exit
```

## File Outputs

All files are saved in the current directory:

- `tech_stack_recommendations_YYYYMMDD_HHMMSS.txt`
- `tech_stack_export_YYYYMMDD_HHMMSS.json`
- `kanban_your_project_name.json`
- `kanban_your_project_name_YYYYMMDD_HHMMSS.md`

## Re-running the Agent

You can run the agent multiple times:
- For different project ideas
- As requirements change
- To explore alternative stacks

Each run creates new timestamped files, so nothing gets overwritten.

## Troubleshooting

**Q: Module not found error?**  
A: Run `pip install -r requirements.txt`

**Q: Permission denied on run_agent.sh?**  
A: Run `chmod +x bot/run_agent.sh`

**Q: No recommendations generated?**  
A: Use more specific keywords in your answers

**Q: Kanban board not saving?**  
A: Check write permissions in the directory

---

## Need Help?

Check the full documentation: `bot/README.md`

🎉 **Ready to build your next project!**

