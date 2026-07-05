# sing-box rule-sets for various services

## Services

| Service               | Description                          |
| --------------------- | ------------------------------------ |
| Discord               | Domains and subnets                  |
| Instagram             | Domains                              |
| LinkedIn              | Domains                              |
| Netflix               | Domains                              |
| OpenAI                | Domains                              |
| Copilot               | Domains                              |
| Grok                  | Domains                              |
| YouTube               | Domains                              |
| X                     | Domains                              |
| TikTok                | Domains                              |
| Telegram              | Domains and subnets                  |
| Spotify               | Domains                              |
| RKN                   | Domains blocked in Russia            |
| Unavailable in Russia | Domains that block users from Russia |
| Roblox                | Domains and subnets                  |
| WhatsApp              | Domains and subnets                  |
| Nintendo              | Domains                              |
| Gemini                | Domains                              |
| Claude                | Domains                              |

> [!NOTE]
> `Unavailable in Russia` rule-set is automatically synced with [dartraiden/no-russia-hosts](https://github.com/dartraiden/no-russia-hosts). Domains from Claude, OpenAI, Gemini, Grok and Netflix rulesets are also merged automatically. Copilot, Spotify and TikTok are intentionally excluded - not everyone needs them.

## File variants

Some services have multiple rule-set files:

| File                          | Contents                                                   |
| ----------------------------- | ---------------------------------------------------------- |
| `discord-full`                | Domains, voice chat subnets and ports - use this if unsure |
| `discord-domains`             | Domains only                                               |
| `discord-voice-chats`         | Voice chat subnets and UDP port range                      |
| `discord-voice-chats-no-cidr` | Voice chat UDP port range only, without subnets            |
| `telegram`                    | Domains and subnets                                        |
| `telegram-voice-chats`        | Voice chat subnets and ports                               |

Plain-text domain lists (one domain per line) for every rule-set are available in the [raw](raw) directory.

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
