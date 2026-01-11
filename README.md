# sing-box rule-sets for various services

## Services

| Service               | Description                                                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Discord               | Domains, voice subnets                                                                                                                      |
| Instagram             | Domains                                                                                                                                     |
| LinkedIn              | Domains                                                                                                                                     |
| Netflix               | Domains                                                                                                                                     |
| OpenAI                | Domains                                                                                                                                     |
| Copilot               | Domains                                                                                                                                     |
| Grok                  | Domains                                                                                                                                     |
| YouTube               | Domains                                                                                                                                     |
| X                     | Domains                                                                                                                                     |
| TikTok                | Domains                                                                                                                                     |
| Telegram              | Voice/video chat subnets                                                                                                                    |
| RKN                   | Domains blocked in Russia                                                                                                                   |
| Unavailable in Russia | Domains that block users from Russia. Automatically synced with [dartraiden/no-russia-hosts](https://github.com/dartraiden/no-russia-hosts) |
| Roblox                | Domains and game server subnets                                                                                                             |
| WhatsApp              | Domains and voice/video chat subnets                                                                                                        |

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
