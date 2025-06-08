Week 1: Planning & Design
Read the Spec & Sketch Ideas

Review the simplified RPG requirements (golden path, scoring, hazards).

In your logbook, note initial thoughts and any questions.

Git Commit #1: Create repository, add README with project overview and Part A goals.

Draft the Storyboard (6–8 Frames)

Sketch each key screen include the flow between each frame

Create UML Class Diagram

Recreate the mermaid code class diagram

Show relationships: inheritance, aggregation, composition, dependency.


Week 2: Flowcharts & Initial Coding
Draw Three Flowcharts

Movement: Start “move <direction>,” check exit, handle blocking droid (hazard increment), or update location.

Use Tool: Start “use tool,” verify possession, check/repair droid.

Win: Start “win,” confirm location + crystal, award bonus or block.

Begin Core Class stubs

Create empty class files for each:

StationItem.py, DiagnosticTool.py, EnergyCrystal.py

Location.py, DamagedMaintenanceDroid.py, Player.py, GameController.py

In each file, define class name with empty methods.

Create markdown files (minimum CHANGELOG.md, PRD.md, TODO,md)
Git Commit: Push markdown files and class stubs with TODO comments for each method.

Implement Location & Droid Logic

In Location.py, implement __init__, add_exit(), describe(), remove_tool(), remove_crystal(), set_droid_present().

In DamagedMaintenanceDroid.py, implement __init__, repair(), is_blocking().

Git Commit: Commit completed Location and Droid classes, with initial unit tests in a separate tests/ folder.


Week 3: Finalise Coding, Testing & Documentation
Complete Player & GameController Logic

In Player.py, implement __init__, move(), pick_up_tool(), use_tool_on_droid(), pick_up_crystal(), get_status().

In GameController.py, implement __init__, start_game(), process_input(), check_win_condition().

Git Commit: Push Player and GameController implementations with inline comments.

Testing & Evidence Collection

Write a test plan with at least five scenarios:

Move while blocked

Pick up tool

Use tool on droid

Pick up crystal

Win sequence

Capture screenshots or console transcripts for each scenario.

Git Commit #8: Add test scripts and sample run logs under tests/.

Embed Final Deliverables in Report

Insert the polished UML diagram, flowcharts, and storyboard into your report.

Include the final, well‐commented Python code.

Git Commit: Commit the final code in repo.

Logbook & Reflection

Ensure your logbook covers every session, including any AI help (include original vs edited code).

Write a one‐page reflection on challenges (OOP concepts, debugging) and what you learned from AI usage.

Git Commit #10: Add the completed logbook file and reflection section to repo.

Final Review & Submission Preparation

Proofread the report: Australian spelling, clear labels, consistent formatting.

Git Commit: Tag final commit as PartA_Final.

2. Submission Instructions
Private GitHub Repo:

Ensure you have made at least 10 substantial commits (as above).

Repository should be shared only with the instructor.

Canvas Upload by 30 June 2025:

Export all .py files and related folders (e.g., tests/) into a ZIP file named YourName_PartA.zip.

Upload that ZIP to Canvas under the Part A assignment by midnight (AEST) 30 June 2025.