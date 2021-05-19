![Meya build](https://github.com/meya-ai/grid-template-hello-world/workflows/Meya%20build/badge.svg)

# Fitness demo

A demo app that includes integrations with Zendesk Help Center, Zendesk Support, Zendesk Chat, and Meya's Orb Live Chat.

The bot helps users connect devices to their fitness apps, and collect information before escalating to a human agent. It can also customize the support experience for users depending on attributes like whether they are a free vs paid user.
      
[Watch demo](https://www.loom.com/share/f632ce7b8f50403e92cf2c82bcbd61e8)

## Setup
[Quick start guide](https://docs.meya.ai/docs/fitness-quick-start-guide)

```shell script
brew install python@3 libgit2
MEYA_AUTH_TOKEN=your_meya_auth_token
MEYA_APP_ID=app-your_app_id
# you can optionally setup a venv instead as well
python3 -m venv venv  # optional
. venv/bin/activate  # optional
pip3 install --upgrade \
    --extra-index-url https://meya:$MEYA_AUTH_TOKEN@grid.meya.ai/registry/pypi \
    "pygit2>=1.2.1" \
    "meya-sdk>=2.0.0" \
    "meya-cli>=2.0.0"
# auth (if needed)
meya auth add --auth-token $MEYA_AUTH_TOKEN
# connect to existing app
meya connect --app-id $MEYA_APP_ID
```

### Integration guides
* [Zendesk Chat](https://docs.meya.ai/docs/how-to-set-up-a-zendesk-chat-integration)
* [Zendesk Support](https://docs.meya.ai/docs/how-to-set-up-a-zendesk-support-integration)
* [Zendesk Help Center](https://docs.meya.ai/docs/zendesk-help-center)
* [Orb](https://docs.meya.ai/docs/how-to-set-up-an-orb-integration)

## Workflow
```shell script 
meya check
meya format
meya test --watch
# to download secrets
meya vault download --file vault.secret.yaml
# if new secrets (after changing the yaml file)
meya vault upload --file vault.secret.yaml
meya push --watch
# for a full rebuild (useful for production deployments)
meya push --force --build-image
```
