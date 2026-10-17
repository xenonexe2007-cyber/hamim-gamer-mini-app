# HAMIM GAMER Telegram Mini App — Render + GitHub

## Included
- `bot.py`: Telegram `/start` bot with an **OPEN HAMIM GAMER** Mini App button.
- `requirements.txt`: Python dependency.
- `render.yaml`: Render Blueprint starter.
- `index.html`: Replace this starter file with your complete HAMIM GAMER HTML.

## Important
Telegram Mini Apps require a public **HTTPS** URL. The bot service and the HTML page are separate deployments:
1. Deploy the `index.html` as a **Render Static Site** (or another HTTPS static host).
2. Deploy this repository as a **Render Web Service** for the bot.
3. Set `WEBAPP_URL` in the bot service to the published Static Site URL.

## Phone-only setup

### A. Put the HTML on Render Static Site
1. In GitHub, create a repository such as `hamim-gamer-mini-app`.
2. Upload your complete HTML as `index.html` at the repository root. Replace the included starter `index.html`.
3. On Render, choose **New + → Static Site**, connect the repository, and select the repository.
4. Set **Build Command** to blank (if Render allows) and **Publish Directory** to `.`.
5. Deploy. Copy the public URL, which should begin with `https://`.

### B. Run the Telegram bot on Render
1. Upload `bot.py`, `requirements.txt`, and `render.yaml` to the GitHub repository.
2. On Render choose **New + → Web Service**, connect the repository.
3. Runtime: Python. Build command: `pip install -r requirements.txt`. Start command: `python bot.py`.
4. In **Environment**, add:
   - `BOT_TOKEN` = token from @BotFather
   - `WEBAPP_URL` = the HTTPS URL of your published Static Site
5. Deploy and wait for **Live** status.
6. Open your bot in Telegram and send `/start`.

## Keep the token private
- Never put your bot token in `bot.py`, `index.html`, GitHub files, or screenshots.
- If the token was shared publicly, revoke it in @BotFather and create a new one.

## Note about free hosting
Render's free Web Services may spin down when idle, so a polling bot can be unavailable until the service wakes again. Check the current Render plan/limitations in your dashboard.
