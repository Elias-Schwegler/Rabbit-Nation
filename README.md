# Rabbit-Nation
Rabbit Nation ist mein Beitrag zum HackSTAIR Game Jam 2025 – einer schweizweiten Online-Challenge für innovative Game-Entwicklung. Ziel: In einem Monat ein einzigartiges Spiel zum Thema „leave something behind“ erschaffen!


# Set-Up:

```txt
https://api.arcade.academy/en/stable/get_started/install.html
```

**conda-Befehl** für ein neues 3.9 empfohlEnvironment mit der korrekten Python-Version für Arcade (mindestens Python en):

```bash
conda create -n arcade-dev python=3.11
```

- Das Environment heißt hier `arcade-dev` (kann beliebig angepasst werden).
- **Python 3.11** ist voll kompatibel mit der aktuellen Arcade-Version und bietet moderne Features.
- Nach der Erstellung aktivierst du das Environment mit:
  ```bash
  conda activate arcade-dev
  ```
- Danach installierst du Arcade mit:
  ```bash
  pip install arcade
  ```

Das reicht für eine schnelle, saubere Umgebung für dein Projekt!





# Project Management from Perplexity, vy best toll and helper.

Here’s a **high-level project plan** for your Indie Game (Arcade, Conda, VSC) based on the execution steps you mentioned. This will serve as a practical, modular roadmap for development and delivery.

***

## 1. Project Setup

- **Create and initialize git repo** (done).
- **Set up Conda environment** for Arcade and dependencies *(done - repeatable for teammates)*.
- **Set up workspace in VSC** (Visual Studio Code) with basic folder structure:
  - `/src`
  - `/assets`
  - `/docs`
  - `/tests`
- **Install Arcade** and auxiliary libraries.
- **Configure `.gitignore`** for Python, Conda envs, and assets.

- [ ] **Project Setup**  
  - [ ] Initialize git repository  
  - [ ] Set up Conda environment  
  - [ ] Install Arcade and dependencies  
  - [ ] Prepare VS Code workspace  
  - [ ] Configure `.gitignore`  


***

## 2. Story & Lore Planning

- **High-level game concept**: a one-page game summary → world, genre, and elevator pitch.
- **Design main characters & world lore**: bullet-style notes or mind-map.
- **Draft story/quest progression**: outline core quest line plus optional sidequests.
- **Decide on tone, visual, and music style**.

- [ ] **Story & Lore Planning**  
  - [ ] Write high-level concept summary  
  - [ ] Create world lore and main characters  
  - [ ] Outline story and quest flow  
  - [ ] Decide on tone and style  

***

## 3. Asset Requirements & Management

- **List all required assets**:
  - Characters (player, NPCs, enemies)
  - Environments (platform tiles, backgrounds)
  - UI elements (menus, buttons, dialogue boxes)
  - Audio (FX, ambience, music)
- **Decide make/buy/source** per asset (draw, commission, or free packs?).
- **Prepare file naming and organization rules** for `/assets`.

- [ ] **Asset Requirements & Management**  
  - [ ] Make list of required assets (character, environment, UI, audio, etc.)  
  - [ ] Decide make/buy/source per asset  
  - [ ] Set naming and folder rules for /assets  

***

## 4. Development & Integration Steps

- **Prototype core systems first**:
  - Player movement (Top-Down + Sprite-Rotation)
  - Basic map (static or tile-based platform)
  - Basic interaction (collision, UI input)
- **Integrate core assets & placeholders**
- **Rapid iteration:**
  - Add features one by one (combat, inventory, dialogue, enemy AI, etc.)
  - Keep the game runnable after every small change
- **Regularly commit & push code** for version control

- [ ] **Development & Integration**  
  - [ ] Prototype core systems (movement, map, input)  
  - [ ] Integrate placeholder assets  
  - [ ] Develop and add new features sequentially  
  - [ ] Frequently commit and push code  

***

## 5. Playtesting & Mechanic Verification

- **Unit-test basic mechanics (movement, combat, collision)**
- **Manual playtest each milestone**: Identify bugs and fun killers early.
- **Iterate & Playtest loops**: Regularly test changed/new mechanics.
- **Collect feedback**: from friends, online or via Discord/itch.io devlog.

- [ ] **Testing of Mechanics & Playtesting**  
  - [ ] Write unit tests for core mechanics  
  - [ ] Manual playtest after each milestone  
  - [ ] Get/collect feedback from testers  
  - [ ] Iterate on mechanics based on feedback  

***

## 6. Story, Quest & Content Integration

- **Implement story beats and quest triggers** (using simple data, e.g. JSON or CSV).
- **Integrate & test progression mechanics** (unlock, NPC dialogue, etc.).
- **Polish narrative presentation** (timing, visuals, music cues).

- [ ] **Story, Quest & Content Integration**  
  - [ ] Implement story beats and quest system  
  - [ ] Integrate narrative events, dialogue, unlocks  
  - [ ] Polish presentation (timing, visuals, audio cues)  

***

## 7. Final Asset Integration & Polish

- **Replace placeholders with finalized assets**.
- **Optimize asset loading & organization**.
- **Add visual/audio polish where needed** (particles, transitions, feedback).

- [ ] **Final Asset Integration & Polish**  
  - [ ] Replace placeholders with finalized assets  
  - [ ] Optimize asset loading and visuals  
  - [ ] Add polish (effects, transitions, feedback)  

***

## 8. Playtesting, QA & Bugfixes

- **Full playthroughs** (internal and external) for flow testing.
- **Polish & bugfix** based on feedback.
- **Performance & compatibility checks**.

- [ ] **Full Playtesting & Bugfixes**  
  - [ ] Complete internal and external playtests  
  - [ ] Bugfix and final performance checks  

***

## 9. Publishing & Release

- **Export/Build distributable** (Windows EXE, HTML5 if supported).
- **Prepare itch.io page** (screenshots, GIFs, description, tags).
- **Upload build and set pricing** (pay-what-you-want or demo/free).
- **Announce release** (socials, devlog, Discord, etc.).
- **Post-release patching** (optional, based on first user feedback).

- [ ] **Publishing & Release**  
  - [ ] Export/build for chosen platforms  
  - [ ] Prepare itch.io/store page  
  - [ ] Upload build and assets  
  - [ ] Announce release and collect first feedback  
  - [ ] Apply post-release patches (if needed)  

***

**Tip:**  
Track all high-level tasks in a simple kanban (e.g. GitHub Projects, Trello, Notion) and keep requirements and ideas in `GAMEPLAN.md`.  
For each phase use rapid, playable prototypes as milestones!
