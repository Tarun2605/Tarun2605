# GitHub Profile README Setup Guide

This repository contains automated workflows for maintaining an up-to-date GitHub profile README with daily statistics and dynamic content.

## 🚀 Features

- **Daily Stats Updates**: Automatically updates date, time, and activity metrics
- **Snake Game Animation**: Generates contribution graph snake animation
- **Blog Posts Integration**: Fetches latest blog posts from Dev.to and Medium
- **WakaTime Stats**: Shows coding time and language statistics (optional)
- **Spotify Integration**: Displays currently playing music (optional)
- **Dynamic Content**: Profile views, GitHub stats, and activity tracking

## 📋 Setup Instructions

### 1. Repository Setup

1. Fork or create a new repository with your GitHub username as the repository name (e.g., `YourUsername/YourUsername`)
2. Ensure the repository is public
3. Copy all files from this setup to your repository

### 2. GitHub Actions Setup

The following workflows are automatically configured:

#### Core Workflows (No setup required):
- **update-readme.yml**: Updates daily stats and recent activity
- **snake.yml**: Generates contribution graph snake animation
- **blog-posts.yml**: Fetches latest blog posts

#### Optional Workflows (Require secrets):

##### WakaTime Integration:
1. Create a [WakaTime](https://wakatime.com) account
2. Get your API key from WakaTime settings
3. Add `WAKATIME_API_KEY` to your repository secrets

##### Spotify Integration:
1. Create a [Spotify App](https://developer.spotify.com/dashboard/applications)
2. Get your Client ID and Client Secret
3. Generate a refresh token using [this tool](https://github.com/novatorem/novatorem)
4. Add these secrets to your repository:
   - `SPOTIFY_CLIENT_ID`
   - `SPOTIFY_SECRET_ID`
   - `SPOTIFY_REFRESH_TOKEN`

### 3. Personal Customization

Update the following in `README.md`:

1. **Personal Information**:
   - Replace "Tarun" with your name
   - Update social media links
   - Add your email and portfolio links
   - Customize the about me section

2. **Tech Stack**:
   - Add/remove technology badges
   - Update skills and tools you use

3. **Blog RSS Feeds**:
   - Update RSS feed URLs in `blog-posts.yml`
   - Replace `tarun2605` with your username

4. **GitHub Username**:
   - Replace `Tarun2605` with your GitHub username throughout all files

### 4. Repository Secrets

Go to your repository Settings → Secrets and variables → Actions, and add:

**Required for basic functionality:**
- `GITHUB_TOKEN` (automatically provided)

**Optional for enhanced features:**
- `WAKATIME_API_KEY` (for coding stats)
- `SPOTIFY_CLIENT_ID` (for music status)
- `SPOTIFY_SECRET_ID` (for music status)
- `SPOTIFY_REFRESH_TOKEN` (for music status)

### 5. Permissions

Ensure GitHub Actions have write permissions:
1. Go to Settings → Actions → General
2. Under "Workflow permissions", select "Read and write permissions"
3. Check "Allow GitHub Actions to create and approve pull requests"

## 🔄 Workflow Schedule

- **Daily Stats**: Updates every day at 00:00 UTC
- **Snake Animation**: Generates daily at 02:00 UTC
- **Blog Posts**: Checks for new posts every 12 hours
- **WakaTime**: Updates every 6 hours (if configured)
- **Spotify**: Updates every 10 minutes (if configured)

## 🛠️ Customization

### Adding New Sections

To add new dynamic sections to your README:

1. Add HTML comments as markers:
   ```html
   <!-- SECTION_NAME:START -->
   Content will be replaced here
   <!-- SECTION_NAME:END -->
   ```

2. Update the `update-readme.yml` workflow to replace content between these markers

### Modifying Update Frequency

Edit the `cron` expressions in the workflow files:
- `'0 0 * * *'` = Daily at midnight
- `'0 */6 * * *'` = Every 6 hours
- `'*/10 * * * *'` = Every 10 minutes

### Styling

The README uses:
- GitHub-flavored Markdown
- Shields.io badges
- External APIs for dynamic content
- HTML for advanced formatting

## 📈 Analytics

Track your profile's performance:
- Profile views counter (automatic)
- Repository statistics (automatic)
- Contribution graphs (automatic)
- Custom metrics (can be added)

## 🎨 Themes

Current theme: Tokyo Night
- Can be changed by updating theme parameters in stat URLs
- Available themes: `default`, `radical`, `merko`, `gruvbox`, `tokyonight`, etc.

## 🐛 Troubleshooting

**Workflows not running:**
- Check repository permissions
- Ensure workflows are enabled in Actions tab
- Verify secrets are correctly set

**README not updating:**
- Check workflow run logs in Actions tab
- Ensure proper file permissions
- Verify HTML comment markers are correct

**Missing statistics:**
- Ensure external services (WakaTime, Spotify) are properly configured
- Check API keys and tokens
- Verify RSS feed URLs are accessible

## 🤝 Contributing

Feel free to:
- Submit issues for bugs or feature requests
- Create pull requests for improvements
- Share your customized versions
- Suggest new integrations

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy coding!** 🚀

For questions or support, feel free to open an issue or reach out.
