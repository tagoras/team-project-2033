import jwt, {Bearer} from "jsonwebtoken";

export async function sentSyncrhonousAccessRequest(page){
  console.log(page);
  console.log(document.cookie.substring(10));
    let result = await fetch(`${page}`, {
      method: "POST",
      headers: {
        'Content-Type': 'application/json;charset=utf-8',
        'Authorization': Bearer `${document.cookie.substring(10)}`
      },
    });

    return result.json();
}