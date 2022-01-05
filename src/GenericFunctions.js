export async function sentSyncrhonousAccessRequest(page){
    let result = await fetch(`${page}`, {
      method: "POST",
      headers: {
        'Content-Type': 'application/json;charset=utf-8'
      },
      JWT: document.cookie.substring(10)
    });

    return result.json();
}