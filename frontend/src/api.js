const API_BASE_URL = "https://career-guidance-engine-backend.onrender.com";

export async function sendChat(formData) {
  const res = await fetch(`${API_BASE_URL}/chat`, {
    method: "POST",
    body: formData,
  });

  if (!res.ok) {
    throw new Error("Failed to send chat");
  }

  return await res.json();
}
