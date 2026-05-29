# sing-box rule-sets for various services

## Services

| Service               | Description                                                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Discord               | Domains and subnets                                                                                                                         |
| Instagram             | Domains                                                                                                                                     |
| LinkedIn              | Domains                                                                                                                                     |
| Netflix               | Domains                                                                                                                                     |
| OpenAI                | Domains                                                                                                                                     |
| Copilot               | Domains                                                                                                                                     |
| Grok                  | Domains                                                                                                                                     |
| YouTube               | Domains                                                                                                                                     |
| X                     | Domains                                                                                                                                     |
| TikTok                | Domains                                                                                                                                     |
| Telegram              | Domains and subnets                                                                                                                         |
| RKN                   | Domains blocked in Russia                                                                                                                   |
| Unavailable in Russia | Domains that block users from Russia. Automatically synced with [dartraiden/no-russia-hosts](https://github.com/dartraiden/no-russia-hosts). Domains from Claude, OpenAI, Gemini, Grok and Netflix rulesets are also merged automatically. Copilot, Spotify and TikTok are intentionally excluded - not everyone needs them. |
| Roblox                | Domains and subnets                                                                                                                         |
| WhatsApp              | Domains and subnets                                                                                                                         |
| Nintendo              | Domains                                                                                                                                     |
| Gemini                | Domains                                                                                                                                     |
| Claude                | Domains                                                                                                                                     |

## Example

```json
"route": {
  "rule_set": [
    {
      "tag": "discord",
      "type": "remote",
      "format": "binary",
      "url": "https://github.com/vernette/rulesets/raw/master/srs/discord-full.srs"
    }
  ]
}
```
