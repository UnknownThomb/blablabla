
---

### `README.md`
```markdown
# Ostium Manual-Reply Assistant (Free)

This Replit template fetches trading-related tweets via Nitter RSS, suggests replies with your Ostium referral link, and logs them for manual posting.

## Setup
1. **Import from GitHub**: Provide your repo URL in Replit.
2. **Add Replit Secret**:
   - Key: `X_Config`
   - Value (JSON):
     ```json
     {
       "REFERRAL_LINK": "https://your.ostium.link"
     }
     ```
3. **Install Dependencies**: Replit will auto-install from `requirements.txt`.
4. **Run**: Click **Run**. Suggestions will appear in `manual_reply_suggestions.txt`.

## Usage
Copy the suggested replies into X to engage manually. Enjoy free, worry-free searching!
