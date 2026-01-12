const API_BASE_URL = "https://career-guidance-engine-backend.onrender.com";

export async function sendChat(formData) {
  console.log("DEBUG: API_BASE_URL =", API_BASE_URL);
  console.log("DEBUG: Sending request to:", `${API_BASE_URL}/chat`);

  for (let pair of formData.entries()) {
    console.log("FORM DATA:", pair[0], pair[1]);
  }

  const res = await fetch(`${API_BASE_URL}/chat`, {
    method: "POST",
    body: formData,
  });

  console.log("DEBUG: Response status =", res.status);

  const text = await res.text();
  console.log("DEBUG: Raw response =", text);

  if (!res.ok) {
    throw new Error("Failed to send chat");
  }

  return JSON.parse(text);
}
