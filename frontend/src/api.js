const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

if (!API_BASE_URL) {
  console.error("❌ VITE_API_BASE_URL is undefined");
}

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
