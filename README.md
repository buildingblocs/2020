
# BuildingBloCS 2019 Website

## Development workflow

### Requirements

1. [Jekyll](https://jekyllrb.com/docs/installation/)
2. [Node.js](https://nodejs.org/)
3. [Yarn](https://yarnpkg.com/)

### Setup

```
git clone git@github.com:serverwentdown/buildingblocs.github.io.git
```

Install project dependencies:

```
yarn install
```

### Building CSS from Sass

Only required if you are modifying stylesheets. Start `grunt` (tool to build `.scss` to `.css`) and make it watch for file changes:

```
yarn build watch
```

If you want to just build and exit, do:

```
yarn build
```

### Serve the local website

```
jekyll serve
open http://localhost:4000
```

Visit the [Jekyll docs](https://jekyllrb.com/docs/) for more information on the [directory sturcture](https://jekyllrb.com/docs/structure/).

We strongly encourage for local development as the online commmit could be messy and hard to orgainse. Thank you!
