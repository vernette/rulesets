sing-box rule-sets for various services.

## Services

- Discord (domains, voice chats)
- Instagram
- LinkedIn
- Netflix
- OpenAI (ChatGPT)
- YouTube
- X (Twitter)
- TikTok
- RKN (sites blocked by RKN)
- Unavailable in Russia (sites that blocked users from Russia)

## Examples

### sing-box >= 1.10.x

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
