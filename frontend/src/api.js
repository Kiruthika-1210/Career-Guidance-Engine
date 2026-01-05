export async function sendChat(formData) {
  const res = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    body: formData,
  });

  if (!res.ok) {
    throw new Error("Failed to send chat");
  }

  return await res.json();
}
