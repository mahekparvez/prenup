# Example Output - AI Tech Stack Advisor

This is an example of what the agent produces for a sample project.

## Input

**Project Idea:** "A timeline app for project management"

### Question 1 Answer:
"Web application, need an MVP to test with users in 2-3 months"

### Question 2 Answer:
"We have intermediate experience with JavaScript and React. No existing infrastructure. Budget around $500/month for hosting and services."

### Question 3 Answer:
"Need drag-and-drop timeline editing, real-time collaboration for team members, file attachments, notifications. Expect 1000 users initially, maybe 10k in a year. Would like offline capability for viewing timelines."

---

## Output

### 📊 REQUIREMENTS ANALYSIS

**Project:** A timeline app for project management

- **Platforms:** Web
- **Stage:** MVP
- **Timeline:** Medium (2-3 months)
- **Experience Level:** Intermediate
- **Budget:** Medium
- **Scale:** Medium (1000 → 10k users)

**Features:**
- Real-time collaboration
- File uploads
- Notifications
- Offline functionality

---

### 🎯 TECH STACK RECOMMENDATIONS

#### 🔴 ESSENTIAL (Must Have)

**Frontend Development > Core Languages**
- Tools: HTML5, CSS3, JavaScript (ES6+)
- Why: Essential for web development

**Frontend Development > Frontend Frameworks**
- Tools: Next.js, React
- Why: Production-ready frameworks for experienced developers

**Backend Development > Core Languages**
- Tools: Node.js, Python
- Why: Backend server and API development

**Backend Development > Frameworks / APIs**
- Tools: NestJS, FastAPI, Django
- Why: Scalable backend frameworks with built-in features

**Databases > Relational (SQL)**
- Tools: PostgreSQL
- Why: Versatile database for most use cases

**DevOps / Infrastructure > Version Control**
- Tools: Git, GitHub
- Why: Essential for code management

**DevOps / Infrastructure > Cloud Providers**
- Tools: Vercel, Railway, AWS
- Why: Flexible hosting options

---

#### 🟡 RECOMMENDED (Should Have)

**Frontend Development > State Management**
- Tools: Zustand, Redux Toolkit, React Query
- Why: Efficient state management for complex applications

**Backend Development > Authentication / Authorization**
- Tools: Clerk, Supabase Auth, NextAuth
- Why: Secure user authentication

**Backend Development > API Architecture**
- Tools: WebSockets, GraphQL (Apollo, Yoga)
- Why: Real-time data synchronization

**Backend Development > API Architecture**
- Tools: Serverless Functions
- Why: Handle file uploads efficiently

**Databases > Caching**
- Tools: Redis
- Why: Improve performance with caching

**DevOps / Infrastructure > CI/CD**
- Tools: GitHub Actions
- Why: Automated testing and deployment

**Testing & QA > Unit / Integration Tests**
- Tools: Jest, PyTest, Vitest
- Why: Ensure code quality and reliability

**Project Management / Collaboration > Agile Tools**
- Tools: Linear, Notion, Trello
- Why: Track tasks and collaborate with team

---

#### 🟢 OPTIONAL (Nice to Have)

**Testing & QA > E2E / UI Testing**
- Tools: Playwright, Cypress
- Why: End-to-end testing for critical user flows

---

#### 🤖 AI TOOLS RECOMMENDATIONS

1. **🔴 Cursor** (HIGH PRIORITY)
   - Category: General Coding
   - Why: Best-in-class AI IDE with deep codebase understanding

2. **🔴 Claude 3.5** (HIGH PRIORITY)
   - Category: General Coding
   - Why: Excellent for complex problem-solving and architecture

3. **🟡 Windsurf**
   - Category: Frontend Development - Core Languages
   - Why: Specialized for core languages

4. **🟡 GitHub Copilot**
   - Category: Frontend Development - Core Languages
   - Why: Specialized for core languages

5. **🟡 v0 by Vercel**
   - Category: Frontend Development - Styling & Preprocessors
   - Why: Specialized for styling & preprocessors

6. **🟡 Galileo AI**
   - Category: Frontend Development - Styling & Preprocessors
   - Why: Specialized for styling & preprocessors

7. **🟡 CodiumAI**
   - Category: Frontend Development - Frontend Frameworks
   - Why: Specialized for frontend frameworks

8. **🟡 Bolt.new**
   - Category: Frontend Development - Frontend Frameworks
   - Why: Specialized for frontend frameworks

9. **🟡 Continue.dev**
   - Category: Frontend Development - State Management
   - Why: Specialized for state management

10. **🟡 Pieces.app**
    - Category: Frontend Development - State Management
    - Why: Specialized for state management

...and 5 more AI tools

---

### 📝 CUSTOM PROMPTS FOR YOUR PROJECT

#### 🔧 SETUP PROMPTS

**Prompt #1: Core Languages Setup**
```
I'm building A timeline app for project management. I need to set up Core Languages.

Project context:
- Platform(s): web
- Stage: MVP
- Timeline: medium
- Tech stack: HTML5, CSS3, JavaScript (ES6+)

Please help me:
1. Set up HTML5, CSS3, JavaScript (ES6+) with best practices
2. Configure the project structure
3. Set up any necessary configuration files
4. Provide a simple example to verify the setup works

Focus on mvp best practices and keep it suitable for a medium timeline.
```

**Prompt #2: Frontend Frameworks Setup**
```
I'm building A timeline app for project management. I need to set up Frontend Frameworks.

Project context:
- Platform(s): web
- Stage: MVP
- Timeline: medium
- Tech stack: Next.js, React

Please help me:
1. Set up Next.js, React with best practices
2. Configure the project structure
3. Set up any necessary configuration files
4. Provide a simple example to verify the setup works

Focus on mvp best practices and keep it suitable for a medium timeline.
```

**Prompt #3: Core Languages Setup**
```
I'm building A timeline app for project management. I need to set up Core Languages.

Project context:
- Platform(s): web
- Stage: MVP
- Timeline: medium
- Tech stack: Node.js, Python

Please help me:
1. Set up Node.js, Python with best practices
2. Configure the project structure
3. Set up any necessary configuration files
4. Provide a simple example to verify the setup works

Focus on mvp best practices and keep it suitable for a medium timeline.
```

...and 4 more setup prompts

---

#### 💻 FEATURE DEVELOPMENT PROMPTS

**Prompt #1: Real-time collaboration**
```
I'm implementing Real-time collaboration for my web application: A timeline app for project management.

Requirements:
- Platform: web
- Scale: medium scale (medium number of users)
- Experience level: intermediate

Please help me:
1. Design the architecture for Real-time collaboration
2. Recommend the best libraries/services
3. Provide implementation guidance with code examples
4. Explain best practices and potential pitfalls

Keep the solution appropriate for intermediate developers.
```

**Prompt #2: File uploads**
```
I'm implementing File uploads for my web application: A timeline app for project management.

Requirements:
- Platform: web
- Scale: medium scale (medium number of users)
- Experience level: intermediate

Please help me:
1. Design the architecture for File uploads
2. Recommend the best libraries/services
3. Provide implementation guidance with code examples
4. Explain best practices and potential pitfalls

Keep the solution appropriate for intermediate developers.
```

...and 2 more feature prompts

---

#### 🤖 AI TOOL USAGE PROMPTS

**Prompt #1: Cursor**
```
I'm using Cursor to help build A timeline app for project management.

Project context:
- Category: General Coding
- Use case: Best-in-class AI IDE with deep codebase understanding

Show me how to effectively use Cursor for:
1. A timeline app for project management
2. Best practices for this tool
3. Example prompts I can use
4. Common mistakes to avoid
```

**Prompt #2: Claude 3.5**
```
I'm using Claude 3.5 to help build A timeline app for project management.

Project context:
- Category: General Coding
- Use case: Excellent for complex problem-solving and architecture

Show me how to effectively use Claude 3.5 for:
1. A timeline app for project management
2. Best practices for this tool
3. Example prompts I can use
4. Common mistakes to avoid
```

...and 3 more AI tool prompts

---

### 📋 KANBAN BOARD

#### 📝 To Do (15 tasks)

**🔴 [T001] Setup Core Languages**
- Category: Frontend Development
- Tools: HTML5, CSS3, JavaScript (ES6+)
- Description: Essential for web development. Implement: HTML5, CSS3, JavaScript (ES6+)

**🔴 [T002] Setup Frontend Frameworks**
- Category: Frontend Development
- Tools: Next.js, React
- Description: Production-ready frameworks for experienced developers. Implement: Next.js, React

**🔴 [T003] Setup Core Languages**
- Category: Backend Development
- Tools: Node.js, Python
- Description: Backend server and API development. Implement: Node.js, Python

**🔴 [T004] Setup Frameworks / APIs**
- Category: Backend Development
- Tools: NestJS, FastAPI, Django
- Description: Scalable backend frameworks with built-in features. Implement: NestJS, FastAPI, Django

**🔴 [T005] Setup Relational (SQL)**
- Category: Databases
- Tools: PostgreSQL
- Description: Versatile database for most use cases. Implement: PostgreSQL

**🔴 [T006] Setup Version Control**
- Category: DevOps / Infrastructure
- Tools: Git, GitHub
- Description: Essential for code management. Implement: Git, GitHub

**🔴 [T007] Setup Cloud Providers**
- Category: DevOps / Infrastructure
- Tools: Vercel, Railway, AWS
- Description: Flexible hosting options. Implement: Vercel, Railway, AWS

**🟡 [T008] Setup State Management**
- Category: Frontend Development
- Tools: Zustand, Redux Toolkit, React Query
- Description: Efficient state management for complex applications. Implement: Zustand, Redux Toolkit, React Query

**🟡 [T009] Setup Authentication / Authorization**
- Category: Backend Development
- Tools: Clerk, Supabase Auth, NextAuth
- Description: Secure user authentication. Implement: Clerk, Supabase Auth, NextAuth

...and 6 more tasks

---

### 📊 Progress Summary

**15/15 tasks created (0% completed)**

Tasks by priority:
- 🔴 High: 7 tasks
- 🟡 Medium: 6 tasks
- 🟢 Low: 2 tasks

Tasks by category:
- Frontend Development: 2 tasks
- Backend Development: 4 tasks
- Databases: 1 task
- DevOps / Infrastructure: 3 tasks
- Features: 4 tasks
- Testing & QA: 1 task

---

## Files Generated

1. **tech_stack_recommendations_20250108_123045.txt** - Full text report (100+ lines)
2. **tech_stack_export_20250108_123045.json** - Structured data (500+ lines)
3. **kanban_a_timeline_app_for_project_management.json** - Kanban board data
4. **kanban_a_timeline_app_for_project_management_20250108_123045.md** - Kanban in Markdown

---

## What To Do Next

1. **Start with Setup Prompts**
   - Copy the first 3-4 setup prompts into Cursor
   - Follow the instructions to set up your project structure

2. **Install Essential Tools**
   - Set up Next.js + React
   - Configure PostgreSQL
   - Set up Git repository

3. **Use the Kanban Board**
   - Open the JSON file to track progress
   - Move tasks from "To Do" → "In Progress" → "Done"

4. **Implement Features**
   - Use the feature development prompts
   - Real-time collaboration first (highest impact)
   - Then file uploads and notifications

5. **Test and Deploy**
   - Set up Jest for testing
   - Deploy to Vercel for MVP

6. **Iterate**
   - Collect user feedback
   - Re-run the agent for production recommendations
   - Scale up as needed

---

**Total Analysis Time:** ~30 seconds  
**Total Recommendations:** 25+ tools across 10+ categories  
**Custom Prompts Generated:** 15+  
**Tasks Created:** 15  

🎉 **Ready to build!**

