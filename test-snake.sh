#!/bin/bash

echo "🐍 Testing Snake Animation Generation"
echo "====================================="

echo "📋 Current GitHub Actions workflow files:"
ls -la .github/workflows/

echo ""
echo "📝 Snake workflow content:"
cat .github/workflows/snake.yml

echo ""
echo "🔍 Checking if output branch exists:"
git branch -r | grep output || echo "Output branch not found - this is normal for first run"

echo ""
echo "📊 Your contribution graph should be available at:"
echo "https://github.com/Tarun2605/Tarun2605/graphs/contributors"

echo ""
echo "🚀 To manually trigger the snake workflow:"
echo "1. Go to https://github.com/Tarun2605/Tarun2605/actions"
echo "2. Click on 'Generate Snake Game' workflow"
echo "3. Click 'Run workflow' button"
echo "4. Wait for it to complete"
echo "5. Check if 'output' branch is created"

echo ""
echo "⚡ The snake animation will be available at:"
echo "https://github.com/Tarun2605/Tarun2605/blob/output/github-contribution-grid-snake.svg"
