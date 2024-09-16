[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AHFn7Vbn)
# Superjoin Hiring Assignment

### Welcome to Superjoin's hiring assignment! 🚀

### Objective
Build a solution that enables real-time synchronization of data between a Google Sheet and a specified database (e.g., MySQL, PostgreSQL). The solution should detect changes in the Google Sheet and update the database accordingly, and vice versa.

### Problem Statement
Many businesses use Google Sheets for collaborative data management and databases for more robust and scalable data storage. However, keeping the data synchronised between Google Sheets and databases is often a manual and error-prone process. Your task is to develop a solution that automates this synchronisation, ensuring that changes in one are reflected in the other in real-time.

### Requirements:
1. Real-time Synchronisation
  - Implement a system that detects changes in Google Sheets and updates the database accordingly.
   - Similarly, detect changes in the database and update the Google Sheet.
  2.	CRUD Operations
   - Ensure the system supports Create, Read, Update, and Delete operations for both Google Sheets and the database.
   - Maintain data consistency across both platforms.
   
### Optional Challenges (This is not mandatory):
1. Conflict Handling
- Develop a strategy to handle conflicts that may arise when changes are made simultaneously in both Google Sheets and the database.
- Provide options for conflict resolution (e.g., last write wins, user-defined rules).
    
2. Scalability: 	
- Ensure the solution can handle large datasets and high-frequency updates without performance degradation.
- Optimize for scalability and efficiency.

## Submission ⏰
The timeline for this submission is: **Next 2 days**

Some things you might want to take care of:
- Make use of git and commit your steps!
- Use good coding practices.
- Write beautiful and readable code. Well-written code is nothing less than a work of art.
- Use semantic variable naming.
- Your code should be organized well in files and folders which is easy to figure out.
- If there is something happening in your code that is not very intuitive, add some comments.
- Add to this README at the bottom explaining your approach (brownie points 😋)
- Use ChatGPT4o/o1/Github Co-pilot, anything that accelerates how you work 💪🏽. 

Make sure you finish the assignment a little earlier than this so you have time to make any final changes.

Once you're done, make sure you **record a video** showing your project working. The video should **NOT** be longer than 120 seconds. While you record the video, tell us about your biggest blocker, and how you overcame it! Don't be shy, talk us through, we'd love that.

We have a checklist at the bottom of this README file, which you should update as your progress with your assignment. It will help us evaluate your project.

- [Yes] My code's working just fine! 🥳
- [Yes] I have recorded a video showing it working and embedded it in the README ▶️
- [Yes] I have tested all the normal working cases 😎
- [Somewhat] I have even solved some edge cases (brownie points) 💪
- [Yes] I added my very planned-out approach to the problem at the end of this README 📜

## Got Questions❓
Feel free to check the discussions tab, you might get some help there. Check out that tab before reaching out to us. Also, did you know, the internet is a great place to explore? 😛

We're available at techhiring@superjoin.ai for all queries. 

All the best ✨.

## Developer's Section
*Add your video here, and your approach to the problem (optional). Leave some comments for us here if you want, we will be reading this :)*



[WhatsApp Video 2024-09-16 at 15.55.26.zip](https://github.com/user-attachments/files/17011512/WhatsApp.Video.2024-09-16.at.15.55.26.zip)


Project Description: Real-Time Synchronization between Google Sheets and MySQL Database

This project is designed to provide real-time synchronization between Google Sheets and a specified MySQL database. It ensures that any changes made in one platform are instantly reflected in the other, enabling a seamless flow of data across both systems. This solution is ideal for businesses and teams that rely on Google Sheets for collaborative data entry and need a robust, scalable database like MySQL for data storage, analytics, and more advanced functionalities.
Key Features:

    Real-Time Synchronization:
        Detects and processes changes in Google Sheets, updating the corresponding entries in the MySQL database.
        Detects changes in the MySQL database, ensuring they are reflected back in Google Sheets without manual intervention.
        Continuous synchronization using threading, checking for updates periodically to maintain up-to-date data on both platforms.

    CRUD Operations:
        Supports full Create, Read, Update, and Delete (CRUD) functionality:
            Create: New rows added in Google Sheets are automatically inserted into the MySQL database, and vice versa.
            Read: Data is fetched from both platforms to ensure consistency.
            Update: Changes in existing data, whether in Google Sheets or the MySQL database, are propagated to the other platform in real-time.
            Delete: Deletions in Google Sheets or the database are mirrored in the counterpart, ensuring no stale data persists.
        Ensures data consistency across both platforms, avoiding duplication or conflicts.

    Scalability and Efficiency:
        Optimized to handle large datasets and high-frequency updates without performance degradation.
        The solution processes only necessary updates by comparing the state of the data before and after any changes, preventing redundant synchronization cycles.
        Real-time sync intervals can be adjusted for more frequent or less frequent updates based on system demands.

    Partial Row Handling:
        Partially filled rows in Google Sheets are not synchronized to the MySQL database until all required fields are complete, preventing incomplete data from being saved.
        The system ensures that partially filled rows do not vanish or cause synchronization errors.

    Conflict Handling (Optional):
        A conflict detection mechanism can be implemented to handle cases where simultaneous changes are made in both Google Sheets and the MySQL database.
        Possible conflict resolution strategies:
            Last Write Wins: The last modified data takes precedence.
            User-Defined Rules: Custom rules can be set to handle conflicting updates based on priority or specific conditions.

    Database Integrity:
        Two JSON files are maintained on the MySQL side to track the state of the data before and after changes. Only when discrepancies are detected between the "before" and "after" states is synchronization with Google Sheets triggered, reducing unnecessary operations.

    Ease of Deployment:
        The system uses Google Sheets API for communication with the spreadsheet and is easily deployable using Python for database connectivity and synchronization logic.
        Google OAuth2 authentication is integrated, ensuring secure access to Google Sheets data.

This project aims to streamline data management by automating synchronization, reducing the need for manual data entry and ensuring data consistency across platforms. With a focus on scalability, real-time performance, and optional conflict handling, it provides a robust solution for teams relying on Google Sheets and MySQL databases.

