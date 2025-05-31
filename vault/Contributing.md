# Contributing to Razon

So you have decided to permanently settle in the [[index#the city of knowledge|city of knowledge]]? Well, there are many ways to do this and you should know that every contribution, no matter how small, matters! Thank you for taking the time to improve Razon!

# How to Contribute

## Reporting Issues

You do not need any technical know-how to report issues with Razon - all you need is a [GitHub](https://github.com/) account. To report a problem, go to the [issues section](https://github.com/ProjectRazon/Razon/issues) of Razon's [repository](https://github.com/ProjectRazon/Razon) and create a new issue with the provided template. If the issue is specific to a given page, you can also use the comment section under it, although this is discouraged. Ideally, all issues should be submitted via GitHub's bug report system.

## Requesting Features

Contributions to Razon can come in many forms and feature requests are one of them. If you have an idea about a feature or improvement you would like to see in Razon but do not have the time or ability to implement it yourself, you can submit a feature request by creating an [issue](https://github.com/ProjectRazon/Razon/issues) on the [repository](https://github.com/ProjectRazon/Razon) using the feature request template.

## Improving the Project

Perhaps the greatest contribution you can make to Razon is by submitting a commit to the project. 

>[!TIP]- Tip: Trello Boards
>
>If you just want to help out but have nothing specific in mind, you can checkout the [[https://trello.com/w/razon_/|Trello board]] to get a grasp of what the project currently needs.
>

### Prerequisites

Before you can contribute to Razon, you should be familiar with the tools which make such a project possible. All content is written in [[https://www.markdownguide.org/|Markdown]] using [[https://obsidian.md/|Obsidian]] and then built into a static website using [[https://quartz.jzhao.xyz/|Quartz]].

The source control system behind Razon is [[https://git-scm.com/|git]], the repository itself is hosted [[https://github.com/MihailKovachev/Razon|here]] using [[https://github.com/|GitHub]]. Currently, the repository is split into three branches:
-  `content` is responsible for handling edits to raw Markdown content, i.e. changes in the `vault` folder;
- `quartz` is responsible for handling configuration and design changes to the website, i.e. changes in the `quartz` folder;
- `main` handles the website build. Currently, a [[https://github.com/MihailKovachev/Razon/blob/content/.github/workflows/deploy.yml|GitHub workflow]] is responsible for automatically building the website from the Markdown content whenever a push is made to the `main` branch. 

### Getting Started

The first thing you need to do is create a [[https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo|fork]] of [[https://github.com/MihailKovachev/Razon|Razon's repository]]. 

If you plan on editing or adding content, you should import the `vault` folder as an Obsidian vault and make all of your changes inside it using the Obsidian editor. Once you are done, you should submit your changes as a [[https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests|pull request]] to the `content` branch.

If you want to fix a bug or add a feature to the website, you should familiarise yourself with [[https://quartz.jzhao.xyz/|Quartz]]. Any such changes should only affect the `quartz` folder and should be submitted as a pull request to the `quartz` branch.

### Testing and Building

In general, if the content you write is rendered correctly in Obsidian, it will also be rendered correctly on the website. However, you should still check if this is the case. If you are building the website for the first time, you need to change into the `quartz` directory and then run

```bash
npm i
```

After this, you can build and host the website locally by executing the following command (again in the `quartz` directory).

```bash
npx quartz build -d ../vault --serve
```

If you are building on Windows, you have to use

```bash
npx quartz build -d ..\vault --serve
```

### Styleguides

All submitted content should abide by the following guidelines in order to ensure that it is of the highest quality:
- Content should be succinct. Avoid unnecessary fluff.
- Content should contain all necessary formalism but also provide the intuition behind it.
- Content should provide plenty of examples and diagrams.
- Content should include a list of references and sources.
- Grammatically correct writing is always a plus.

#### Organising Content

Each separate concept should be put in its own page. Folders should be used to group related or similar pages together but only loosely. Each note should be marked with tags which indicate the broad topics which are discussed in the note.

#### Links

Links are specified with the usual Markdown syntax `(link text)[url]` and *not* as [[https://help.obsidian.md/Linking+notes+and+files/Internal+links#Supported+formats+for+internal+links|wikilinks]]. All internal links should be relative. When your page relies on a concept or term from another page, *all* of its occurrences should link to the page which explains it.

#### Callouts

[[https://help.obsidian.md/Editing+and+formatting/Callouts|Callouts]] are a feature of Obsidian but integrate seamlessly with Quartz. They are rendered as colourful blocks of content on the page and are extremely handy when organising content and focusing attention. As such, you should strive to use them as much as possible. 

There are a few different valid syntaxes for specifying callouts, but only the following one should be used in Razon to ensure consistency:

```
>[!CALLOUTTYPE] Optional Title
>Callout content
>
```

<!-- Quartz's renderer currently has an issue which appends an additional "greater than" sign before "Callout content" if the correct syntax for a callout is written in a code block. Hence, the above code block actually contains incorrect callout syntax, but will be rendered correctly as a code block. Nevertheless, this issue does not extend to actual callouts and so you should use the proper syntax when specifying them. -->

The `CALLOUTTYPE` is a single word, written in CAPS, which indicates the type of callout to be created. Callouts can also be made collapsible by appending `+` or `-` directly to `[!CALLOUT TYPE]`, without spaces. If `+` is used, the callout will be unfolded by default. If `-` is used, then the callout will be folded by default. 

>[!NOTE] Note: Supported Callouts
>
>Currently, Razon supports all callout types provided by Obsidian and Quartz as well as the following custom callouts: `DEFINITION`, `INTUITION`, `NOTATION`, `ALGORITHM`, `AXIOM`, `THEOREM`, `PROOF`, `CONSTANT`, `UNIT` and `LAW`.
>

After this, there should be a single space, followed by an optional title for the callout. This title should have the format `CalloutType: Actual Title`. You can also omit the title entirely and then the callout type will be rendered as the title.

Each new line of the content should be preceded by a `>` symbol. There should be an empty line directly before the content and directly after it. Otherwise, there will be errors in rendering.

You can also nest callouts. Apply the above guidelines to each nested callout as well.

#### Examples

Examples are very useful but usually lengthy and can thus hinder readability. Hence, all examples should be provided as collapsible, folded by default, [[Contributing#callouts|callouts]] of the type `EXAMPLE`.

#### Intuition

The content of a page should ideally introduce all necessary formalism and provide explanations in a subsequent collapsible, folded by default, [[Contributing#callouts|callout]] of the `INTUITION` type. This is done because intuitions behind concepts can be long-winded and hinder the readability of the page.
