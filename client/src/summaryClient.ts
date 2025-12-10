export interface SummaryRequest {
  text: string;
}

export interface SummaryResponse {
  summary: string;
  timestamp: string;
  wordCount: number;
}

type ServerSummaryResponse = Omit<SummaryResponse, "wordCount">;

export async function createSummary(
  baseURL: string,
  payload: SummaryRequest,
): Promise<SummaryResponse> {
  let response: Response | null = null;
  try {
    response = await fetch(`${baseURL}/summaries`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(payload),
    });
  } catch (error) {
    throw new Error(
      "Failed to connect to the server. Please check the baseURL or your network connection.",
    );
  }

  if (!response.ok) {
    throw new Error(
      `Request failed with status ${response.status} ${response.statusText}`,
    );
  }

  const data = (await response.json()) as Awaited<ServerSummaryResponse>;

  // Calculate word count in the client side.
  const wordCount = data.summary.trim().split(/\s+/).length;

  return { ...data, wordCount };
}
