# Skitter

## Sprint 1

1. `POST /signIn`
    - Input: RIT username, RIT password
    - Output: success, sessionID, message: user_info {lastname, firstname} if successful, or error message otherwise.
    - This needs to get the following information from the RIT LDAP server and put it into the database along with the generated session ID.
        - Lastname
        - Firstname
    - This will only insert a new session into the `SESSION` table. No information is inserted to the `USER_INFO` table at this point.
2. `GET /isAuthenticated`
    - Input: RIT username, sessionID
    - Output: success, text
    - This will utilize the `SESSION` table and lookup for the entry using both the RIT username and the session ID.
3. `POST /newUser`
    - Input: RIT username, firstname, lastname, username.
    - Output: success, message
    - This will attempt to insert new data into the `USER_INFO` table if the user hasn't had an account.
4. `GET /deleteUser`
    - Input: RIT username
    - Output:
    - Action:
5. Dockerize this thing.
