# Free Fire Bio Update Discord Bot

This Discord bot allows users to update Free Fire bios using the Flexbase-Long-Bio-Api.

## Prerequisites

- Python 3.8 or higher
- The Free Fire API server running on `http://127.0.0.1:5000`

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Set the environment variables:
   - First, get a Discord bot token:
     1. Go to https://discord.com/developers/applications
     2. Create a new application
     3. Create a bot under the application
     4. Copy the token from the "Token" section
     5. Add the bot to your server using the OAuth2 URL generator
   
   - Windows:
   ```cmd
   set DISCORD_BOT_TOKEN=YOUR_VALID_DISCORD_BOT_TOKEN_HERE
   set API_BASE_URL=http://127.0.0.1:5000
   ```
   - Linux/Mac:
   ```bash
   export DISCORD_BOT_TOKEN="YOUR_VALID_DISCORD_BOT_TOKEN_HERE"
   export API_BASE_URL="http://127.0.0.1:5000"
   ```

## Usage

Run the bot:
```bash
python bot.py
```

## Deploying the API Online

To host the API online using Vercel:

1. Install the Vercel CLI:
```bash
npm install -g vercel
```

2. Navigate to the main project directory (where app.py and vercel.json are located):
```bash
cd ../
```

3. Deploy to Vercel:
```bash
vercel --prod
```

4. After deployment, update the `API_BASE_URL` environment variable with your Vercel URL:
   - Windows:
   ```cmd
   set API_BASE_URL=https://your-vercel-url.vercel.app
   ```
   - Linux/Mac:
   ```bash
   export API_BASE_URL="https://your-vercel-url.vercel.app"
   ```

5. If your API is not working after deployment, make sure the vercel.json configuration is correct and redeploy:
   - Check that the vercel.json file exists and has the correct configuration
   - Run `vercel --prod` again to redeploy

### Commands

- `!bio <uid> <password> <bio_text>` - Updates the Free Fire bio using UID and password
- `!bio_jwt <jwt_token> <bio_text>` - Updates the Free Fire bio using JWT token
- `!bio_access <access_token> <bio_text>` - Updates the Free Fire bio using access token
- `!help_ff` - Shows help information

### Examples

```
!bio 1234567890 mypassword123 This is my new bio!
!bio_jwt eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... My JWT bio!
!bio_access access_token123 Another bio!
```

## Important Security Notice

- Keep your Discord bot token secure
- Never share account credentials in public channels
- The bot transmits account information to update the bio, so only use in private channels if possible