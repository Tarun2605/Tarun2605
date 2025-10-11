# 🛠️ Quick Customization Script

import os
import re

def customize_profile():
    """
    Quick customization script for GitHub profile README
    """
    
    print("🚀 GitHub Profile README Customization")
    print("=" * 50)
    
    # Get user information
    username = input("Enter your GitHub username: ").strip()
    name = input("Enter your display name: ").strip()
    email = input("Enter your email (optional): ").strip()
    linkedin = input("Enter your LinkedIn username (optional): ").strip()
    twitter = input("Enter your Twitter handle (optional): ").strip()
    portfolio = input("Enter your portfolio URL (optional): ").strip()
    
    # Read current README
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print("❌ README.md not found!")
        return
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update username references
    if username:
        content = re.sub(r'Tarun2605', username, content)
        print(f"✅ Updated GitHub username to: {username}")
    
    # Update display name
    if name:
        content = re.sub(r"I'm Tarun!", f"I'm {name}!", content)
        print(f"✅ Updated display name to: {name}")
    
    # Update contact information
    if email:
        content = re.sub(r'your-email@example\.com', email, content)
        print(f"✅ Updated email to: {email}")
    
    if linkedin:
        content = re.sub(r'linkedin\.com/in/your-profile', f'linkedin.com/in/{linkedin}', content)
        print(f"✅ Updated LinkedIn to: {linkedin}")
    
    if twitter:
        content = re.sub(r'twitter\.com/your-handle', f'twitter.com/{twitter}', content)
        print(f"✅ Updated Twitter to: {twitter}")
    
    if portfolio:
        content = re.sub(r'https://your-portfolio\.com', portfolio, content)
        print(f"✅ Updated portfolio to: {portfolio}")
    
    # Write updated README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Update workflow files
    workflow_files = [
        '.github/workflows/blog-posts.yml',
        '.github/workflows/wakatime.yml'
    ]
    
    for workflow_file in workflow_files:
        if os.path.exists(workflow_file):
            with open(workflow_file, 'r', encoding='utf-8') as f:
                workflow_content = f.read()
            
            if username:
                workflow_content = re.sub(r'tarun2605', username.lower(), workflow_content)
            
            with open(workflow_file, 'w', encoding='utf-8') as f:
                f.write(workflow_content)
            
            print(f"✅ Updated {workflow_file}")
    
    print("\n🎉 Customization complete!")
    print("\n📋 Next steps:")
    print("1. Push these changes to your GitHub repository")
    print("2. Enable GitHub Actions in your repository settings")
    print("3. Set up optional integrations (WakaTime, Spotify) if desired")
    print("4. Check the SETUP.md file for detailed instructions")

if __name__ == "__main__":
    customize_profile()
