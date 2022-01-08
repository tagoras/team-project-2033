import jwt, {Bearer} from "jsonwebtoken";

export async function sentSyncrhonousAccessRequest(page, method){
  console.log(page);
  console.log(document.cookie.substring(10));
  let string = document.cookie.substring(10);
    let result = await fetch(`${page}`, {
      method: `${method}`,
      headers: {
        'Content-Type': 'application/json;charset=utf-8',
        'Authorization': `Bearer ${document.cookie.substring(10)}`
      },
    });

    return result.json();
}

// eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0MTQwMzM3MywianRpIjoiNTEyNWI0ZDUtZjBlZi00YjRiLWIyNzktMmE0ZWViNTAwODE5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwicG9zdGNvZGUiOiJwYmtkZjI6c2hhMjU2OjI2MDAwMCRBOWhMblhsclh2aEp6eFI2JDg1ZTRiZjI2ZDgzMGI3OWViZGYyN2UyNDczMjg0NGE4M2I3ZDBjOTM0ZGI1MzdkOGU4ZWM3MjA1ZDg4ODM4MjEiLCJ1c2VybmFtZSI6IkpvZSIsImVtYWlsIjoidGVzdDFAdGVzdC5jb20iLCJyb2xlIjoiYWRtaW4ifSwibmJmIjoxNjQxNDAzMzczLCJleHAiOjE2NDE0MDQyNzN9.qfMYJE6wTz9lGOuVGXretn3aQnkee5b6yuILOJ0nMic
