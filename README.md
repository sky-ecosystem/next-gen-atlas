# Next-Generation Atlas

Contains data for the currently-in-development Next-Generation Atlas.

Used for testing the Atlas-Axis edit flow without impacting the official [sky-ecosystem/next-gen-atlas](https://github.com/sky-ecosystem/next-gen-atlas).

Nothing should be contributed from this repository.

## CI/CD

All workflows run on [Blacksmith](https://blacksmith.sh/) GitHub Actions runners. Workflows are defined in `.github/workflows/` and run automatically:

- **Validate Atlas** (`validate-atlas.yml`): Runs on every pull request. Validates `Sky Atlas/Sky Atlas.md` using the [atlas-validator](https://github.com/Atlas-Axis/atlas-validator) action.
- **Notify Private Mirror** (`notify-private.yml`): Triggers on push to `main`. Dispatches a sync event to the private working repo.

### Support

For build failures or CI issues, reach out on **#tech-engineering** on Discord.
