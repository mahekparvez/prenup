"""
AI Agent for Tech Stack Recommendations
Takes user's idea, asks 3 questions, provides personalized tech stack recommendations
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Tuple
import re
from kanban_tracker import VibeKanban, create_kanban_from_agent, interactive_kanban_manager

# Tech Stack Database
TECH_STACK = {
    "Frontend Development": {
        "Core Languages": {
            "tools": ["HTML5", "CSS3", "JavaScript (ES6+)", "TypeScript", "JSX"],
            "ai_tools": ["Cursor", "Windsurf", "GitHub Copilot", "Cody (Sourcegraph)", "Tabnine", 
                        "Replit Ghostwriter", "Codeium", "Amazon CodeWhisperer", "ChatGPT (GPT-5)", 
                        "Claude 3.5", "Devin AI"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "beginner"
        },
        "Styling & Preprocessors": {
            "tools": ["Tailwind CSS", "Bootstrap", "Material UI", "Chakra UI", "Bulma", 
                     "SASS/SCSS", "LESS", "PostCSS", "Emotion", "Styled Components"],
            "ai_tools": ["v0 by Vercel", "Galileo AI", "Uizard", "Relume", "Figma AI", 
                        "Diagram", "Penpot AI", "Magic Patterns", "Locofy", "Fronty", "TeleportHQ"],
            "use_cases": ["web", "mobile"],
            "complexity": "beginner"
        },
        "Frontend Frameworks": {
            "tools": ["React", "Next.js", "Vue.js", "Nuxt", "Angular", "Svelte", "Qwik", "Solid.js", "Astro"],
            "ai_tools": ["Cursor", "Windsurf", "Copilot", "CodiumAI", "Bolt.new", "CodeAssist", 
                        "Aidev.codes", "Blackbox AI", "Cognition Devin", "Amazon Q Developer"],
            "use_cases": ["web"],
            "complexity": "intermediate"
        },
        "State Management": {
            "tools": ["Redux Toolkit", "Zustand", "MobX", "Recoil", "React Query", "Apollo Client", 
                     "XState", "Jotai", "Pinia (Vue)", "NgRx (Angular)"],
            "ai_tools": ["Cursor", "Claude", "Copilot Labs", "Continue.dev", "Pieces.app", 
                        "GPT Engineer", "Cody", "OpenDevin", "Sweep AI", "AutoDev"],
            "use_cases": ["web"],
            "complexity": "intermediate"
        },
        "UI/UX Design & Components": {
            "tools": ["Figma", "Adobe XD", "Sketch", "Framer", "Storybook", "Shadcn/UI", 
                     "Ant Design", "Radix", "MUI", "Fluent"],
            "ai_tools": ["Figma AI", "Galileo AI", "Uizard", "v0 by Vercel", "Relume", 
                        "Visual Copilot (Builder.io)", "Diagram", "Magician (Figma)", 
                        "Genius UI", "TeleportHQ"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "beginner"
        },
        "Frontend Build Tools": {
            "tools": ["Webpack", "Vite", "Rollup", "Parcel", "Babel", "Snowpack", "Gulp", "Grunt", "Turbopack"],
            "ai_tools": ["Windsurf", "Cursor", "Codeium", "ChatGPT", "Cody", "AutoCode", 
                        "Continue.dev", "JetBrains AI", "Sourcery AI", "Phind Code"],
            "use_cases": ["web"],
            "complexity": "advanced"
        }
    },
    "Backend Development": {
        "Core Languages": {
            "tools": ["Node.js", "Python", "Go", "Rust", "Java", "Kotlin", "C#", "Ruby", "PHP", "Elixir"],
            "ai_tools": ["Cursor", "GitHub Copilot", "Codeium", "ChatGPT", "Windsurf", "Tabnine", 
                        "Blackbox AI", "Amazon Q", "Devin AI", "Cody"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "intermediate"
        },
        "Frameworks / APIs": {
            "tools": ["Express.js", "NestJS", "Fastify", "Django", "Flask", "FastAPI", 
                     "Spring Boot", "Laravel", "Ruby on Rails", "Fiber (Go)", "Actix (Rust)"],
            "ai_tools": ["Cursor", "Claude", "Copilot Labs", "Phind", "CodeGeeX", "AutoCode", 
                        "Continue.dev", "JetBrains AI", "Aider", "Replit Ghostwriter"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "intermediate"
        },
        "Authentication / Authorization": {
            "tools": ["Auth0", "Clerk", "Supabase Auth", "Firebase Auth", "NextAuth", 
                     "OAuth2", "JWT", "Keycloak", "Okta", "Passport.js"],
            "ai_tools": ["Claude", "Cursor", "ChatGPT", "Copilot", "DevGPT", "SecureGPT", 
                        "Protect AI", "AutoSec", "Aider", "Phind"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "intermediate"
        },
        "Data / ORM / Validation": {
            "tools": ["Prisma", "Sequelize", "TypeORM", "Mongoose", "SQLAlchemy", "Drizzle ORM", "Zod", "Joi"],
            "ai_tools": ["Cursor", "Claude", "Windsurf", "Copilot Labs", "Tabnine", "GPT Engineer", 
                        "AutoDev", "Phind", "OpenDevin", "Devin AI"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "intermediate"
        },
        "Background Jobs / Queues": {
            "tools": ["BullMQ", "Celery", "RabbitMQ", "Kafka", "Temporal", "Redis Queue", 
                     "Resque", "AWS SQS", "Google Pub/Sub"],
            "ai_tools": ["ChatGPT", "Claude", "Cursor", "Copilot", "Phind", "JetBrains AI", 
                        "Blackbox", "Continue.dev", "AutoGPT", "DevChat"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "advanced"
        },
        "API Architecture": {
            "tools": ["REST", "GraphQL (Apollo, Yoga)", "tRPC", "gRPC", "WebSockets", 
                     "Webhooks", "Serverless Functions"],
            "ai_tools": ["Cursor", "Claude", "Windsurf", "Copilot", "Postman AI", "RapidAPI AI", 
                        "Hoppscotch AI", "Aider", "Codeium", "Amazon Q"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "intermediate"
        },
        "Security / Middleware": {
            "tools": ["Helmet.js", "CSRF", "CORS", "Rate Limiter", "bcrypt", "JWT rotation", "dotenv", "ACLs"],
            "ai_tools": ["Protect AI", "Claude", "Sentinel AI", "GitGuardian AI", "Socket.dev AI", 
                        "Checkmarx AI", "DeepCode", "Snyk AI", "Cursor", "Copilot"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "advanced"
        }
    },
    "Databases": {
        "Relational (SQL)": {
            "tools": ["PostgreSQL", "MySQL", "SQLite", "MariaDB", "MS SQL Server", "CockroachDB", "Neon"],
            "ai_tools": ["Text2SQL (OpenAI)", "DataPilot", "Dataherald", "MindsDB", "PopSQL AI", 
                        "Cube AI", "Count.co", "SQLChat", "Tabnine", "DBeaver AI"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "intermediate"
        },
        "NoSQL": {
            "tools": ["MongoDB", "DynamoDB", "CouchDB", "Firebase", "Cassandra", "RedisJSON", "Neo4j"],
            "ai_tools": ["ChatGPT", "Claude", "MindsDB", "LangChain SQL Agent", "Cursor", 
                        "Copilot", "Phind", "TableTalk", "Text2Cypher", "SQLGPT"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "intermediate"
        },
        "Caching": {
            "tools": ["Redis", "Memcached", "KeyDB", "Hazelcast"],
            "ai_tools": ["Claude", "Cursor", "ChatGPT", "Codeium", "Phind", "Copilot", 
                        "JetBrains AI", "Continue.dev", "Devin AI", "Snyk AI"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "advanced"
        },
        "Search Engines": {
            "tools": ["Elasticsearch", "Meilisearch", "Typesense", "Solr", "Algolia"],
            "ai_tools": ["Elastic AI Assistant", "ChatGPT", "Claude", "Cursor", 
                        "LangChain Retriever QA", "Pinecone Assistant", "Weaviate AI", 
                        "Vespa AI", "Devin AI", "Codeium"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "advanced"
        }
    },
    "DevOps / Infrastructure": {
        "Version Control": {
            "tools": ["Git", "GitHub", "GitLab", "Bitbucket", "Mercurial"],
            "ai_tools": ["GitHub Copilot", "CodiumAI", "JetBrains AI", "DevGPT", "ChatGPT", 
                        "Claude", "Sourcegraph Cody", "Continue.dev", "AutoCode", "Sweep AI"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "beginner"
        },
        "CI/CD": {
            "tools": ["GitHub Actions", "Jenkins", "CircleCI", "Travis", "Drone", "ArgoCD", 
                     "Semaphore", "Buildkite"],
            "ai_tools": ["Codefresh AI", "Harness AI", "AWS CodeCatalyst", "Claude", "ChatGPT", 
                        "Windsurf", "Cursor", "Aider", "Amazon Q", "Jenkins AI"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "advanced"
        },
        "Containerization": {
            "tools": ["Docker", "Podman"],
            "ai_tools": ["ChatGPT", "Claude", "Windsurf", "DevGPT", "Copilot", "Cursor", 
                        "K8sGPT", "DockrGPT", "Phind", "AutoDeployer"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "advanced"
        },
        "Orchestration": {
            "tools": ["Kubernetes", "OpenShift", "Nomad"],
            "ai_tools": ["K8sGPT", "Robusta AI", "Komodor AI", "ChatGPT", "Claude", "Phind", 
                        "Lens AI", "Opsera AI", "DevGPT", "CloudZero AI"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "advanced"
        },
        "Cloud Providers": {
            "tools": ["AWS", "Azure", "Google Cloud", "Oracle Cloud", "DigitalOcean", 
                     "Vercel", "Railway", "Fly.io", "Render", "Cloudflare"],
            "ai_tools": ["Amazon Q", "Azure Copilot", "Google Gemini Code Assist", "ChatGPT", 
                        "Claude", "Cursor", "Harness AI", "CloudQuery AI", "DevGPT", "Kubiya AI"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "intermediate"
        },
        "Infrastructure as Code (IaC)": {
            "tools": ["Terraform", "Ansible", "Pulumi", "AWS CDK", "Chef"],
            "ai_tools": ["Terraform AI", "Pulumi Copilot", "Claude", "ChatGPT", "DevGPT", 
                        "Windsurf", "Phind", "Copilot", "AutoDeployer", "JetBrains AI"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "advanced"
        },
        "Monitoring / Logging": {
            "tools": ["Prometheus", "Grafana", "Loki", "Sentry", "New Relic", "Datadog", 
                     "Logtail", "CloudWatch"],
            "ai_tools": ["Sentry AI", "Datadog AI Insights", "Claude", "ChatGPT", "Grafana Loki AI", 
                        "Robusta AI", "Prometheus Advisor", "DevGPT", "Amazon Q", "Cursor"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "advanced"
        }
    },
    "Mobile App Development": {
        "Cross Platform": {
            "tools": ["React Native", "Flutter", "Ionic", "NativeScript", "Expo"],
            "ai_tools": ["Cursor", "Windsurf", "Copilot", "v0 by Vercel", "Replit Ghostwriter", 
                        "Uizard", "Galileo", "Claude", "ChatGPT", "Appypie AI"],
            "use_cases": ["mobile"],
            "complexity": "intermediate"
        },
        "Native": {
            "tools": ["Swift (iOS)", "Kotlin (Android)", "Objective-C", "Java"],
            "ai_tools": ["Xcode AI", "Kotlin Assistant", "ChatGPT", "Claude", "Copilot", 
                        "Replit Ghostwriter", "Phind", "JetBrains AI", "Cursor", "Codeium"],
            "use_cases": ["mobile"],
            "complexity": "advanced"
        },
        "Mobile UI / UX": {
            "tools": ["Figma", "Framer", "Lottie", "ProtoPie"],
            "ai_tools": ["Figma AI", "Relume", "Uizard", "Galileo AI", "Diagram", "Magician", 
                        "v0 by Vercel", "Visily", "Fronty", "Builder.io Copilot"],
            "use_cases": ["mobile"],
            "complexity": "beginner"
        },
        "Testing / Deployment": {
            "tools": ["Detox", "Appium", "Firebase Test Lab", "TestFlight", "Play Console"],
            "ai_tools": ["Testim.io AI", "Mabl", "Appium AI", "ChatGPT", "Claude", "CodiumAI", 
                        "Cursor", "TestGPT", "LambdaTest AI", "Waldo.ai"],
            "use_cases": ["mobile"],
            "complexity": "advanced"
        }
    },
    "Testing & QA": {
        "Unit / Integration Tests": {
            "tools": ["Jest", "Mocha", "PyTest", "Vitest", "NUnit", "xUnit"],
            "ai_tools": ["CodiumAI", "Testim.io", "Mabl", "ChatGPT", "Claude", "Cursor", 
                        "Copilot", "Windsurf", "Continue.dev", "AutoTest AI"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "intermediate"
        },
        "E2E / UI Testing": {
            "tools": ["Cypress", "Playwright", "Selenium", "Puppeteer", "Katalon"],
            "ai_tools": ["Testim AI", "Mabl", "Waldo.ai", "TestGPT", "Claude", "ChatGPT", 
                        "Cursor", "Copilot", "Codeium", "QA Wolf AI"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "intermediate"
        },
        "Load & Security Testing": {
            "tools": ["Locust", "k6", "JMeter", "OWASP ZAP", "Burp Suite"],
            "ai_tools": ["StackHawk AI", "Protect AI", "Claude", "ChatGPT", "Copilot", 
                        "Snyk AI", "GitGuardian AI", "DeepCode", "CodeQL AI", "Checkmarx AI"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "advanced"
        }
    },
    "Security & Compliance": {
        "App Security": {
            "tools": ["Helmet.js", "CSP", "Rate Limiting", "2FA", "HSTS"],
            "ai_tools": ["Protect AI", "GitGuardian AI", "Snyk AI", "Socket.dev AI", "Claude", 
                        "ChatGPT", "Guardrails AI", "Fortify AI", "AquaSec AI", "Phind"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "advanced"
        },
        "Data Security & Compliance": {
            "tools": ["SSL/TLS", "Hashing (bcrypt, Argon2)", "Encryption (AES, RSA)", 
                     "GDPR", "HIPAA", "SOC2"],
            "ai_tools": ["SecureGPT", "Protect AI", "Claude", "ChatGPT", "AutoSec", "Sentinel AI", 
                        "Cyberhaven AI", "AWS Macie AI", "Google DLP AI", "DevGPT"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "advanced"
        }
    },
    "Analytics & BI": {
        "Product Analytics": {
            "tools": ["PostHog", "Mixpanel", "Amplitude", "Segment", "Plausible"],
            "ai_tools": ["Amplitude AI", "PostHog Assistant", "ChatGPT", "Claude", "Copilot", 
                        "LangChain Analytics Agent", "DataGPT", "Metabase AI", "Tableau GPT", 
                        "Power BI Copilot"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "intermediate"
        },
        "Data Visualization / BI": {
            "tools": ["Tableau", "Power BI", "Looker", "Metabase", "Superset"],
            "ai_tools": ["Tableau GPT", "Power BI Copilot", "ChatGPT", "Claude", "DataGPT", 
                        "Vizly AI", "Explo AI", "Synthesia Data AI", "DashGPT", "Sigma AI"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "intermediate"
        }
    },
    "Project Management / Collaboration": {
        "Agile Tools": {
            "tools": ["Jira", "Trello", "Linear", "Asana", "ClickUp", "Notion", "Monday.com"],
            "ai_tools": ["Notion AI", "ClickUp Brain", "Jira Atlassian Intelligence", "ChatGPT", 
                        "Claude", "Linear AI", "Asana AI", "Motion AI", "Taskade AI", "DevGPT"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "beginner"
        },
        "Documentation / Communication": {
            "tools": ["Confluence", "Slack", "Discord", "Google Docs", "Notion"],
            "ai_tools": ["Notion AI", "Slack GPT", "Google Gemini", "ChatGPT", "Claude", 
                        "GrammarlyGO", "Otter AI", "Fireflies", "Fathom", "Copilot for M365"],
            "use_cases": ["web", "mobile", "desktop"],
            "complexity": "beginner"
        }
    }
}

# Questions to ask users
QUESTIONS = [
    {
        "id": "q1",
        "question": """Question 1: What platform(s) do you need this app for (web, mobile iOS/Android, or desktop), 
and are you looking to build an MVP to test the concept or a production-ready application? 
What's your target timeline for launch?""",
        "keywords": {
            "web": ["web", "website", "browser", "online"],
            "mobile": ["mobile", "ios", "android", "app", "phone", "smartphone"],
            "desktop": ["desktop", "windows", "mac", "linux", "electron"],
            "mvp": ["mvp", "prototype", "poc", "proof of concept", "test", "minimum viable"],
            "production": ["production", "prod", "scale", "enterprise", "full-featured"],
            "timeline_short": ["week", "weeks", "quick", "fast", "asap", "urgent"],
            "timeline_medium": ["month", "months", "2 months", "3 months"],
            "timeline_long": ["6 months", "year", "long-term"]
        }
    },
    {
        "id": "q2",
        "question": """Question 2: What's your team's technical background and experience level, 
do you have any existing infrastructure or services you need to integrate with, 
and what's your approximate budget range for development and ongoing hosting?""",
        "keywords": {
            "beginner": ["beginner", "learning", "new", "novice", "first time", "no experience"],
            "intermediate": ["intermediate", "some experience", "familiar", "moderate", "decent"],
            "advanced": ["advanced", "expert", "experienced", "senior", "professional", "veteran"],
            "existing_infra": ["existing", "integrate", "legacy", "current system", "infrastructure"],
            "budget_low": ["low budget", "cheap", "free", "minimal cost", "bootstrap", "side project"],
            "budget_medium": ["medium budget", "moderate", "reasonable", "startup"],
            "budget_high": ["high budget", "enterprise", "unlimited", "well-funded", "large budget"]
        }
    },
    {
        "id": "q3",
        "question": """Question 3: What specific features do you envision (drag-and-drop editing, real-time collaboration, 
file attachments, notifications), how many users do you expect initially and at scale, 
and do you need offline functionality or any specialized requirements like data visualization or integrations with other tools?""",
        "keywords": {
            "realtime": ["real-time", "realtime", "collaboration", "live", "concurrent", "websocket"],
            "offline": ["offline", "offline-first", "local storage", "sync"],
            "file_upload": ["file", "upload", "attachment", "storage", "media"],
            "notifications": ["notification", "alert", "push", "email", "sms"],
            "auth": ["auth", "authentication", "login", "signup", "user management"],
            "analytics": ["analytics", "tracking", "metrics", "dashboard", "reporting"],
            "visualization": ["visualization", "chart", "graph", "data viz", "dashboard"],
            "scale_small": ["small", "few users", "personal", "10 users", "100 users"],
            "scale_medium": ["medium", "1000 users", "thousands", "growing"],
            "scale_large": ["large", "millions", "enterprise", "massive", "10000"]
        }
    }
]


class TechStackAgent:
    """AI Agent that recommends tech stack based on user requirements"""
    
    def __init__(self):
        self.user_idea = ""
        self.answers = {}
        self.analysis = {}
        self.recommendations = {}
        
    def start_session(self, idea: str):
        """Initialize a new recommendation session"""
        self.user_idea = idea
        self.answers = {}
        self.analysis = {}
        self.recommendations = {}
        print(f"\n🚀 Starting tech stack analysis for: '{idea}'\n")
        
    def ask_questions(self) -> Dict[str, str]:
        """Ask the three questions and collect answers"""
        print("Let's understand your requirements better...\n")
        
        for i, q in enumerate(QUESTIONS, 1):
            print(f"\n{q['question']}\n")
            answer = input(f"Your answer: ").strip()
            self.answers[q['id']] = answer
            
        return self.answers
    
    def analyze_answers(self) -> Dict:
        """Analyze user answers and extract key requirements"""
        analysis = {
            "platforms": [],
            "stage": "mvp",
            "timeline": "medium",
            "experience_level": "intermediate",
            "budget": "medium",
            "features": [],
            "scale": "medium",
            "special_requirements": []
        }
        
        # Analyze Q1 - Platform and Timeline
        q1_lower = self.answers['q1'].lower()
        for keyword in QUESTIONS[0]['keywords']['web']:
            if keyword in q1_lower:
                analysis['platforms'].append('web')
                break
        for keyword in QUESTIONS[0]['keywords']['mobile']:
            if keyword in q1_lower:
                analysis['platforms'].append('mobile')
                break
        for keyword in QUESTIONS[0]['keywords']['desktop']:
            if keyword in q1_lower:
                analysis['platforms'].append('desktop')
                break
                
        # Default to web if no platform specified
        if not analysis['platforms']:
            analysis['platforms'] = ['web']
            
        # Determine stage
        for keyword in QUESTIONS[0]['keywords']['mvp']:
            if keyword in q1_lower:
                analysis['stage'] = 'mvp'
                break
        for keyword in QUESTIONS[0]['keywords']['production']:
            if keyword in q1_lower:
                analysis['stage'] = 'production'
                break
                
        # Determine timeline
        for keyword in QUESTIONS[0]['keywords']['timeline_short']:
            if keyword in q1_lower:
                analysis['timeline'] = 'short'
                break
        for keyword in QUESTIONS[0]['keywords']['timeline_long']:
            if keyword in q1_lower:
                analysis['timeline'] = 'long'
                break
        
        # Analyze Q2 - Experience and Budget
        q2_lower = self.answers['q2'].lower()
        for keyword in QUESTIONS[1]['keywords']['beginner']:
            if keyword in q2_lower:
                analysis['experience_level'] = 'beginner'
                break
        for keyword in QUESTIONS[1]['keywords']['advanced']:
            if keyword in q2_lower:
                analysis['experience_level'] = 'advanced'
                break
                
        for keyword in QUESTIONS[1]['keywords']['budget_low']:
            if keyword in q2_lower:
                analysis['budget'] = 'low'
                break
        for keyword in QUESTIONS[1]['keywords']['budget_high']:
            if keyword in q2_lower:
                analysis['budget'] = 'high'
                break
                
        if any(keyword in q2_lower for keyword in QUESTIONS[1]['keywords']['existing_infra']):
            analysis['special_requirements'].append('existing_infrastructure')
        
        # Analyze Q3 - Features and Scale
        q3_lower = self.answers['q3'].lower()
        
        feature_mapping = {
            'realtime': 'Real-time collaboration',
            'offline': 'Offline functionality',
            'file_upload': 'File uploads',
            'notifications': 'Notifications',
            'auth': 'Authentication',
            'analytics': 'Analytics',
            'visualization': 'Data visualization'
        }
        
        for key, feature_name in feature_mapping.items():
            if any(keyword in q3_lower for keyword in QUESTIONS[2]['keywords'][key]):
                analysis['features'].append(feature_name)
                
        for keyword in QUESTIONS[2]['keywords']['scale_small']:
            if keyword in q3_lower:
                analysis['scale'] = 'small'
                break
        for keyword in QUESTIONS[2]['keywords']['scale_large']:
            if keyword in q3_lower:
                analysis['scale'] = 'large'
                break
        
        self.analysis = analysis
        return analysis
    
    def generate_recommendations(self) -> Dict:
        """Generate personalized tech stack recommendations"""
        recommendations = {
            "essential": [],
            "recommended": [],
            "optional": [],
            "ai_tools": []
        }
        
        analysis = self.analysis
        
        # Frontend recommendations
        if 'web' in analysis['platforms']:
            # Core languages are essential
            recommendations['essential'].append({
                "category": "Frontend Development",
                "subcategory": "Core Languages",
                "tools": TECH_STACK["Frontend Development"]["Core Languages"]["tools"][:3],
                "reason": "Essential for web development"
            })
            
            # Framework based on experience
            if analysis['experience_level'] == 'beginner':
                recommendations['essential'].append({
                    "category": "Frontend Development",
                    "subcategory": "Frontend Frameworks",
                    "tools": ["React", "Next.js"],
                    "reason": "Popular, beginner-friendly with great community support"
                })
                recommendations['recommended'].append({
                    "category": "Frontend Development",
                    "subcategory": "Styling & Preprocessors",
                    "tools": ["Tailwind CSS", "Chakra UI"],
                    "reason": "Easy-to-use styling frameworks"
                })
            else:
                recommendations['essential'].append({
                    "category": "Frontend Development",
                    "subcategory": "Frontend Frameworks",
                    "tools": ["Next.js", "React", "Vue.js"],
                    "reason": "Production-ready frameworks for experienced developers"
                })
                recommendations['recommended'].append({
                    "category": "Frontend Development",
                    "subcategory": "State Management",
                    "tools": ["Zustand", "Redux Toolkit", "React Query"],
                    "reason": "Efficient state management for complex applications"
                })
        
        # Mobile recommendations
        if 'mobile' in analysis['platforms']:
            if analysis['experience_level'] in ['beginner', 'intermediate']:
                recommendations['essential'].append({
                    "category": "Mobile App Development",
                    "subcategory": "Cross Platform",
                    "tools": ["React Native", "Expo"],
                    "reason": "Cross-platform development with JavaScript knowledge"
                })
            else:
                recommendations['essential'].append({
                    "category": "Mobile App Development",
                    "subcategory": "Cross Platform",
                    "tools": ["React Native", "Flutter"],
                    "reason": "Powerful cross-platform frameworks"
                })
                recommendations['optional'].append({
                    "category": "Mobile App Development",
                    "subcategory": "Native",
                    "tools": ["Swift (iOS)", "Kotlin (Android)"],
                    "reason": "For platform-specific optimizations"
                })
        
        # Backend recommendations
        recommendations['essential'].append({
            "category": "Backend Development",
            "subcategory": "Core Languages",
            "tools": ["Node.js", "Python"] if analysis['experience_level'] != 'advanced' else ["Node.js", "Python", "Go"],
            "reason": "Backend server and API development"
        })
        
        if 'web' in analysis['platforms'] or 'mobile' in analysis['platforms']:
            if analysis['experience_level'] == 'beginner':
                recommendations['essential'].append({
                    "category": "Backend Development",
                    "subcategory": "Frameworks / APIs",
                    "tools": ["Express.js", "FastAPI"],
                    "reason": "Simple, fast backend frameworks"
                })
            else:
                recommendations['essential'].append({
                    "category": "Backend Development",
                    "subcategory": "Frameworks / APIs",
                    "tools": ["NestJS", "FastAPI", "Django"],
                    "reason": "Scalable backend frameworks with built-in features"
                })
        
        # Database recommendations
        if analysis['scale'] == 'small' and analysis['experience_level'] == 'beginner':
            recommendations['essential'].append({
                "category": "Databases",
                "subcategory": "NoSQL",
                "tools": ["Firebase", "MongoDB"],
                "reason": "Easy-to-use database with quick setup"
            })
        elif analysis['scale'] == 'large' or analysis['stage'] == 'production':
            recommendations['essential'].append({
                "category": "Databases",
                "subcategory": "Relational (SQL)",
                "tools": ["PostgreSQL", "MySQL"],
                "reason": "Robust, scalable relational database"
            })
            recommendations['recommended'].append({
                "category": "Databases",
                "subcategory": "Caching",
                "tools": ["Redis"],
                "reason": "Improve performance with caching"
            })
        else:
            recommendations['essential'].append({
                "category": "Databases",
                "subcategory": "Relational (SQL)",
                "tools": ["PostgreSQL"],
                "reason": "Versatile database for most use cases"
            })
        
        # Authentication
        if 'Authentication' in str(analysis['features']) or analysis['stage'] == 'production':
            recommendations['recommended'].append({
                "category": "Backend Development",
                "subcategory": "Authentication / Authorization",
                "tools": ["Clerk", "Supabase Auth", "NextAuth"] if analysis['budget'] != 'high' else ["Auth0", "Okta"],
                "reason": "Secure user authentication"
            })
        
        # Real-time features
        if 'Real-time collaboration' in analysis['features']:
            recommendations['recommended'].append({
                "category": "Backend Development",
                "subcategory": "API Architecture",
                "tools": ["WebSockets", "GraphQL (Apollo, Yoga)"],
                "reason": "Real-time data synchronization"
            })
        
        # File uploads
        if 'File uploads' in analysis['features']:
            recommendations['recommended'].append({
                "category": "Backend Development",
                "subcategory": "API Architecture",
                "tools": ["Serverless Functions"],
                "reason": "Handle file uploads efficiently"
            })
        
        # Analytics
        if 'Analytics' in analysis['features'] or 'Data visualization' in analysis['features']:
            recommendations['optional'].append({
                "category": "Analytics & BI",
                "subcategory": "Product Analytics",
                "tools": ["PostHog", "Mixpanel", "Plausible"],
                "reason": "Track user behavior and metrics"
            })
        
        if 'Data visualization' in analysis['features']:
            recommendations['optional'].append({
                "category": "Analytics & BI",
                "subcategory": "Data Visualization / BI",
                "tools": ["Metabase", "Superset"],
                "reason": "Create data visualizations and dashboards"
            })
        
        # DevOps recommendations
        recommendations['essential'].append({
            "category": "DevOps / Infrastructure",
            "subcategory": "Version Control",
            "tools": ["Git", "GitHub"],
            "reason": "Essential for code management"
        })
        
        if analysis['stage'] == 'production' or analysis['scale'] != 'small':
            recommendations['recommended'].append({
                "category": "DevOps / Infrastructure",
                "subcategory": "CI/CD",
                "tools": ["GitHub Actions"],
                "reason": "Automated testing and deployment"
            })
        
        # Cloud/Hosting recommendations
        if analysis['budget'] == 'low':
            recommendations['essential'].append({
                "category": "DevOps / Infrastructure",
                "subcategory": "Cloud Providers",
                "tools": ["Vercel", "Railway", "Render"],
                "reason": "Cost-effective hosting with generous free tiers"
            })
        elif analysis['budget'] == 'high' or analysis['scale'] == 'large':
            recommendations['essential'].append({
                "category": "DevOps / Infrastructure",
                "subcategory": "Cloud Providers",
                "tools": ["AWS", "Google Cloud", "Azure"],
                "reason": "Enterprise-grade scalability and features"
            })
        else:
            recommendations['essential'].append({
                "category": "DevOps / Infrastructure",
                "subcategory": "Cloud Providers",
                "tools": ["Vercel", "Railway", "AWS"],
                "reason": "Flexible hosting options"
            })
        
        # Testing recommendations
        if analysis['stage'] == 'production' or analysis['experience_level'] == 'advanced':
            recommendations['recommended'].append({
                "category": "Testing & QA",
                "subcategory": "Unit / Integration Tests",
                "tools": ["Jest", "PyTest", "Vitest"],
                "reason": "Ensure code quality and reliability"
            })
            recommendations['optional'].append({
                "category": "Testing & QA",
                "subcategory": "E2E / UI Testing",
                "tools": ["Playwright", "Cypress"],
                "reason": "End-to-end testing for critical user flows"
            })
        
        # Project management
        recommendations['recommended'].append({
            "category": "Project Management / Collaboration",
            "subcategory": "Agile Tools",
            "tools": ["Linear", "Notion", "Trello"],
            "reason": "Track tasks and collaborate with team"
        })
        
        # AI Tools recommendations
        ai_tools_rec = self._recommend_ai_tools(recommendations)
        recommendations['ai_tools'] = ai_tools_rec
        
        self.recommendations = recommendations
        return recommendations
    
    def _recommend_ai_tools(self, tech_recommendations: Dict) -> List[Dict]:
        """Recommend AI tools based on selected technologies"""
        ai_tools = []
        seen_tools = set()
        
        # General coding assistants (always recommend)
        ai_tools.append({
            "tool": "Cursor",
            "category": "General Coding",
            "reason": "Best-in-class AI IDE with deep codebase understanding",
            "priority": "high"
        })
        
        ai_tools.append({
            "tool": "Claude 3.5",
            "category": "General Coding",
            "reason": "Excellent for complex problem-solving and architecture",
            "priority": "high"
        })
        
        # Extract AI tools from recommendations
        for priority in ['essential', 'recommended', 'optional']:
            for rec in tech_recommendations.get(priority, []):
                category = rec['category']
                subcategory = rec['subcategory']
                
                if category in TECH_STACK and subcategory in TECH_STACK[category]:
                    tech_ai_tools = TECH_STACK[category][subcategory].get('ai_tools', [])
                    
                    # Add top 2-3 AI tools for this category
                    for tool in tech_ai_tools[:3]:
                        if tool not in seen_tools:
                            ai_tools.append({
                                "tool": tool,
                                "category": f"{category} - {subcategory}",
                                "reason": f"Specialized for {subcategory.lower()}",
                                "priority": "medium" if priority == 'essential' else "low"
                            })
                            seen_tools.add(tool)
        
        return ai_tools[:15]  # Limit to top 15 AI tools
    
    def generate_prompts(self) -> Dict[str, List[Dict]]:
        """Generate custom prompts for each recommended tool/category"""
        prompts = {
            "setup_prompts": [],
            "development_prompts": [],
            "ai_tool_prompts": []
        }
        
        # Generate setup prompts
        for rec in self.recommendations.get('essential', []):
            prompt = self._create_setup_prompt(rec)
            prompts['setup_prompts'].append(prompt)
        
        # Generate development prompts based on features
        for feature in self.analysis.get('features', []):
            prompt = self._create_feature_prompt(feature)
            prompts['development_prompts'].append(prompt)
        
        # Generate AI tool usage prompts
        for ai_tool in self.recommendations.get('ai_tools', [])[:5]:  # Top 5
            prompt = self._create_ai_tool_prompt(ai_tool)
            prompts['ai_tool_prompts'].append(prompt)
        
        return prompts
    
    def _create_setup_prompt(self, recommendation: Dict) -> Dict:
        """Create a setup prompt for a technology"""
        tools_str = ", ".join(recommendation['tools'])
        
        prompt_text = f"""I'm building {self.user_idea}. I need to set up {recommendation['subcategory']}.

Project context:
- Platform(s): {', '.join(self.analysis['platforms'])}
- Stage: {self.analysis['stage'].upper()}
- Timeline: {self.analysis['timeline']}
- Tech stack: {tools_str}

Please help me:
1. Set up {tools_str} with best practices
2. Configure the project structure
3. Set up any necessary configuration files
4. Provide a simple example to verify the setup works

Focus on {self.analysis['stage']} best practices and keep it suitable for a {self.analysis['timeline']} timeline."""
        
        return {
            "category": recommendation['subcategory'],
            "tools": recommendation['tools'],
            "prompt": prompt_text
        }
    
    def _create_feature_prompt(self, feature: str) -> Dict:
        """Create a development prompt for a specific feature"""
        platform = self.analysis['platforms'][0] if self.analysis['platforms'] else 'web'
        
        prompt_text = f"""I'm implementing {feature} for my {platform} application: {self.user_idea}.

Requirements:
- Platform: {platform}
- Scale: {self.analysis['scale']} scale ({self.analysis['scale']} number of users)
- Experience level: {self.analysis['experience_level']}

Please help me:
1. Design the architecture for {feature}
2. Recommend the best libraries/services
3. Provide implementation guidance with code examples
4. Explain best practices and potential pitfalls

Keep the solution appropriate for {self.analysis['experience_level']} developers."""
        
        return {
            "feature": feature,
            "prompt": prompt_text
        }
    
    def _create_ai_tool_prompt(self, ai_tool: Dict) -> Dict:
        """Create a prompt for using a specific AI tool"""
        prompt_text = f"""I'm using {ai_tool['tool']} to help build {self.user_idea}.

Project context:
- Category: {ai_tool['category']}
- Use case: {ai_tool['reason']}

Show me how to effectively use {ai_tool['tool']} for:
1. {self.user_idea}
2. Best practices for this tool
3. Example prompts I can use
4. Common mistakes to avoid"""
        
        return {
            "tool": ai_tool['tool'],
            "prompt": prompt_text
        }
    
    def print_analysis(self):
        """Print the analysis results"""
        print("\n" + "="*80)
        print("📊 REQUIREMENTS ANALYSIS")
        print("="*80)
        
        print(f"\n🎯 Project: {self.user_idea}")
        print(f"\n📱 Platforms: {', '.join(self.analysis['platforms'])}")
        print(f"🚦 Stage: {self.analysis['stage'].upper()}")
        print(f"⏱️  Timeline: {self.analysis['timeline'].title()}")
        print(f"👥 Experience Level: {self.analysis['experience_level'].title()}")
        print(f"💰 Budget: {self.analysis['budget'].title()}")
        print(f"📈 Scale: {self.analysis['scale'].title()}")
        
        if self.analysis['features']:
            print(f"\n✨ Features:")
            for feature in self.analysis['features']:
                print(f"   - {feature}")
        
        if self.analysis['special_requirements']:
            print(f"\n🔧 Special Requirements:")
            for req in self.analysis['special_requirements']:
                print(f"   - {req.replace('_', ' ').title()}")
    
    def print_recommendations(self):
        """Print the recommendations"""
        print("\n" + "="*80)
        print("🎯 TECH STACK RECOMMENDATIONS")
        print("="*80)
        
        print("\n🔴 ESSENTIAL (Must Have):")
        for rec in self.recommendations['essential']:
            tools_str = ", ".join(rec['tools'])
            print(f"\n  {rec['category']} > {rec['subcategory']}")
            print(f"  Tools: {tools_str}")
            print(f"  Why: {rec['reason']}")
        
        if self.recommendations['recommended']:
            print("\n\n🟡 RECOMMENDED (Should Have):")
            for rec in self.recommendations['recommended']:
                tools_str = ", ".join(rec['tools'])
                print(f"\n  {rec['category']} > {rec['subcategory']}")
                print(f"  Tools: {tools_str}")
                print(f"  Why: {rec['reason']}")
        
        if self.recommendations['optional']:
            print("\n\n🟢 OPTIONAL (Nice to Have):")
            for rec in self.recommendations['optional']:
                tools_str = ", ".join(rec['tools'])
                print(f"\n  {rec['category']} > {rec['subcategory']}")
                print(f"  Tools: {tools_str}")
                print(f"  Why: {rec['reason']}")
        
        print("\n\n🤖 AI TOOLS RECOMMENDATIONS:")
        for ai_tool in self.recommendations['ai_tools']:
            priority_icon = "🔴" if ai_tool['priority'] == 'high' else "🟡" if ai_tool['priority'] == 'medium' else "🟢"
            print(f"\n  {priority_icon} {ai_tool['tool']}")
            print(f"     Category: {ai_tool['category']}")
            print(f"     Why: {ai_tool['reason']}")
    
    def print_prompts(self, prompts: Dict):
        """Print the generated prompts"""
        print("\n" + "="*80)
        print("📝 CUSTOM PROMPTS FOR YOUR PROJECT")
        print("="*80)
        
        print("\n🔧 SETUP PROMPTS:")
        for i, prompt in enumerate(prompts['setup_prompts'], 1):
            print(f"\n--- Prompt #{i}: {prompt['category']} Setup ---")
            print(prompt['prompt'])
            print()
        
        if prompts['development_prompts']:
            print("\n" + "-"*80)
            print("💻 FEATURE DEVELOPMENT PROMPTS:")
            for i, prompt in enumerate(prompts['development_prompts'], 1):
                print(f"\n--- Prompt #{i}: {prompt['feature']} ---")
                print(prompt['prompt'])
                print()
        
        if prompts['ai_tool_prompts']:
            print("\n" + "-"*80)
            print("🤖 AI TOOL USAGE PROMPTS:")
            for i, prompt in enumerate(prompts['ai_tool_prompts'], 1):
                print(f"\n--- Prompt #{i}: {prompt['tool']} ---")
                print(prompt['prompt'])
                print()
    
    def save_to_file(self, prompts: Dict, filename: str = None):
        """Save all recommendations and prompts to a file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"tech_stack_recommendations_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            f.write("="*80 + "\n")
            f.write(f"TECH STACK RECOMMENDATIONS FOR: {self.user_idea}\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*80 + "\n\n")
            
            # Write analysis
            f.write("📊 REQUIREMENTS ANALYSIS\n")
            f.write("-"*80 + "\n")
            f.write(f"Platforms: {', '.join(self.analysis['platforms'])}\n")
            f.write(f"Stage: {self.analysis['stage'].upper()}\n")
            f.write(f"Timeline: {self.analysis['timeline'].title()}\n")
            f.write(f"Experience Level: {self.analysis['experience_level'].title()}\n")
            f.write(f"Budget: {self.analysis['budget'].title()}\n")
            f.write(f"Scale: {self.analysis['scale'].title()}\n")
            
            if self.analysis['features']:
                f.write(f"\nFeatures:\n")
                for feature in self.analysis['features']:
                    f.write(f"  - {feature}\n")
            
            # Write recommendations
            f.write("\n\n" + "="*80 + "\n")
            f.write("🎯 TECH STACK RECOMMENDATIONS\n")
            f.write("="*80 + "\n\n")
            
            f.write("ESSENTIAL (Must Have):\n")
            f.write("-"*80 + "\n")
            for rec in self.recommendations['essential']:
                tools_str = ", ".join(rec['tools'])
                f.write(f"\n{rec['category']} > {rec['subcategory']}\n")
                f.write(f"Tools: {tools_str}\n")
                f.write(f"Why: {rec['reason']}\n")
            
            if self.recommendations['recommended']:
                f.write("\n\nRECOMMENDED (Should Have):\n")
                f.write("-"*80 + "\n")
                for rec in self.recommendations['recommended']:
                    tools_str = ", ".join(rec['tools'])
                    f.write(f"\n{rec['category']} > {rec['subcategory']}\n")
                    f.write(f"Tools: {tools_str}\n")
                    f.write(f"Why: {rec['reason']}\n")
            
            if self.recommendations['optional']:
                f.write("\n\nOPTIONAL (Nice to Have):\n")
                f.write("-"*80 + "\n")
                for rec in self.recommendations['optional']:
                    tools_str = ", ".join(rec['tools'])
                    f.write(f"\n{rec['category']} > {rec['subcategory']}\n")
                    f.write(f"Tools: {tools_str}\n")
                    f.write(f"Why: {rec['reason']}\n")
            
            f.write("\n\nAI TOOLS RECOMMENDATIONS:\n")
            f.write("-"*80 + "\n")
            for ai_tool in self.recommendations['ai_tools']:
                f.write(f"\n{ai_tool['tool']} [{ai_tool['priority'].upper()}]\n")
                f.write(f"  Category: {ai_tool['category']}\n")
                f.write(f"  Why: {ai_tool['reason']}\n")
            
            # Write prompts
            f.write("\n\n" + "="*80 + "\n")
            f.write("📝 CUSTOM PROMPTS FOR YOUR PROJECT\n")
            f.write("="*80 + "\n\n")
            
            f.write("SETUP PROMPTS:\n")
            f.write("-"*80 + "\n")
            for i, prompt in enumerate(prompts['setup_prompts'], 1):
                f.write(f"\nPrompt #{i}: {prompt['category']} Setup\n")
                f.write("-"*40 + "\n")
                f.write(prompt['prompt'] + "\n\n")
            
            if prompts['development_prompts']:
                f.write("\n\nFEATURE DEVELOPMENT PROMPTS:\n")
                f.write("-"*80 + "\n")
                for i, prompt in enumerate(prompts['development_prompts'], 1):
                    f.write(f"\nPrompt #{i}: {prompt['feature']}\n")
                    f.write("-"*40 + "\n")
                    f.write(prompt['prompt'] + "\n\n")
            
            if prompts['ai_tool_prompts']:
                f.write("\n\nAI TOOL USAGE PROMPTS:\n")
                f.write("-"*80 + "\n")
                for i, prompt in enumerate(prompts['ai_tool_prompts'], 1):
                    f.write(f"\nPrompt #{i}: {prompt['tool']}\n")
                    f.write("-"*40 + "\n")
                    f.write(prompt['prompt'] + "\n\n")
        
        print(f"\n✅ Full report saved to: {filename}")
        return filename
    
    def export_to_json(self, filename: str = None):
        """Export all data to JSON format"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"tech_stack_export_{timestamp}.json"
        
        export_data = {
            "idea": self.user_idea,
            "timestamp": datetime.now().isoformat(),
            "answers": self.answers,
            "analysis": self.analysis,
            "recommendations": self.recommendations,
            "prompts": self.generate_prompts()
        }
        
        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2)
        
        print(f"✅ Data exported to JSON: {filename}")
        return filename


def main():
    """Main function to run the tech stack agent"""
    print("\n" + "="*80)
    print("🚀 WELCOME TO THE AI TECH STACK ADVISOR")
    print("="*80)
    print("\nThis AI agent will help you choose the perfect tech stack for your project!")
    print("I'll ask you 3 questions to understand your needs, then provide personalized")
    print("recommendations with custom prompts for each tool.\n")
    
    # Get user's idea
    idea = input("What's your project idea? (one line): ").strip()
    
    if not idea:
        print("❌ Please provide a project idea!")
        return
    
    # Initialize agent
    agent = TechStackAgent()
    agent.start_session(idea)
    
    # Ask questions
    agent.ask_questions()
    
    # Analyze answers
    print("\n\n🔍 Analyzing your requirements...")
    agent.analyze_answers()
    agent.print_analysis()
    
    # Generate recommendations
    print("\n\n💡 Generating personalized recommendations...")
    agent.generate_recommendations()
    agent.print_recommendations()
    
    # Generate prompts
    print("\n\n✍️  Creating custom prompts for your project...")
    prompts = agent.generate_prompts()
    agent.print_prompts(prompts)
    
    # Save to files
    print("\n\n💾 Saving recommendations...")
    text_file = agent.save_to_file(prompts)
    json_file = agent.export_to_json()
    
    # Create Kanban board
    print("\n\n📋 Creating Kanban board to track your tasks...")
    kanban = create_kanban_from_agent(agent)
    kanban.display_board()
    kanban_md = kanban.export_markdown()
    
    print("\n" + "="*80)
    print("✅ COMPLETE!")
    print("="*80)
    print(f"\nYour personalized tech stack recommendations are ready!")
    print(f"📄 Text report: {text_file}")
    print(f"📊 JSON export: {json_file}")
    print(f"📋 Kanban board: {kanban.board_file}")
    print(f"📝 Kanban markdown: {kanban_md}")
    print(f"\nUse these prompts with your AI coding assistants to get started quickly!")
    
    # Ask if user wants to manage kanban board
    manage = input("\n\nWould you like to manage your Kanban board now? (y/n): ").strip().lower()
    if manage == 'y':
        interactive_kanban_manager(kanban)
    
    print("\n🎉 Happy coding!\n")


if __name__ == "__main__":
    main()

