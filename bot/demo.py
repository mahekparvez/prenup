#!/usr/bin/env python3
"""
Demo script for the AI Tech Stack Advisor
Shows example usage without requiring user input
"""

from tech_stack_agent import TechStackAgent
from kanban_tracker import create_kanban_from_agent

def run_demo():
    """Run a demo of the tech stack agent"""
    
    print("\n" + "="*80)
    print("🎬 DEMO: AI TECH STACK ADVISOR")
    print("="*80)
    print("\nThis demo shows how the agent works with pre-filled answers.\n")
    
    # Create agent
    agent = TechStackAgent()
    
    # Demo project idea
    idea = "A collaborative timeline app for project management"
    print(f"💡 Project Idea: {idea}\n")
    
    agent.start_session(idea)
    
    # Pre-filled answers (simulating user input)
    demo_answers = {
        'q1': "Web application, need an MVP to test with users in 2-3 months. Target launch is mid-2025.",
        'q2': "Team has intermediate experience with JavaScript and React. No existing infrastructure. Budget around $500/month for hosting and services.",
        'q3': "Need drag-and-drop timeline editing, real-time collaboration for team members, file attachments, push notifications. Expect 1000 users initially, maybe 10k in a year. Would like offline capability for viewing timelines."
    }
    
    print("Simulating Q&A session...\n")
    for q_id, answer in demo_answers.items():
        q_num = int(q_id[1])
        print(f"Question {q_num}: {answer}\n")
    
    agent.answers = demo_answers
    
    # Analyze
    print("\n🔍 Analyzing requirements...")
    agent.analyze_answers()
    agent.print_analysis()
    
    # Generate recommendations
    print("\n\n💡 Generating recommendations...")
    agent.generate_recommendations()
    agent.print_recommendations()
    
    # Generate prompts
    print("\n\n✍️  Generating custom prompts...")
    prompts = agent.generate_prompts()
    
    print("\n" + "-"*80)
    print("📝 SAMPLE PROMPTS (showing first 2)")
    print("-"*80)
    
    # Show first 2 setup prompts
    for i, prompt in enumerate(prompts['setup_prompts'][:2], 1):
        print(f"\n--- Setup Prompt #{i}: {prompt['category']} ---")
        print(prompt['prompt'][:300] + "...\n")
    
    # Show first feature prompt
    if prompts['development_prompts']:
        print(f"\n--- Feature Prompt: {prompts['development_prompts'][0]['feature']} ---")
        print(prompts['development_prompts'][0]['prompt'][:300] + "...\n")
    
    # Create Kanban board
    print("\n📋 Creating Kanban board...")
    kanban = create_kanban_from_agent(agent, "demo_kanban.json")
    kanban.display_compact()
    
    # Save files
    print("\n\n💾 Saving outputs...")
    text_file = agent.save_to_file(prompts, "demo_recommendations.txt")
    json_file = agent.export_to_json("demo_export.json")
    
    print("\n" + "="*80)
    print("✅ DEMO COMPLETE!")
    print("="*80)
    print(f"\nGenerated files:")
    print(f"  📄 {text_file}")
    print(f"  📊 {json_file}")
    print(f"  📋 {kanban.board_file}")
    
    print(f"\n📈 Summary:")
    print(f"  - Project: {idea}")
    print(f"  - Platform: {', '.join(agent.analysis['platforms'])}")
    print(f"  - Essential tools: {len(agent.recommendations['essential'])}")
    print(f"  - Recommended tools: {len(agent.recommendations['recommended'])}")
    print(f"  - AI tools: {len(agent.recommendations['ai_tools'])}")
    print(f"  - Custom prompts: {len(prompts['setup_prompts']) + len(prompts['development_prompts']) + len(prompts['ai_tool_prompts'])}")
    print(f"  - Tasks created: {len(kanban.tasks)}")
    
    print("\n🎉 You can now run the full version with: python3 tech_stack_agent.py\n")


if __name__ == "__main__":
    run_demo()

