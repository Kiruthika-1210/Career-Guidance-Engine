console.log("ENV OBJECT 👉", import.meta.env);
console.log("API BASE 👉", import.meta.env.VITE_API_BASE_URL);

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

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
