export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const query = url.searchParams.get("query") || "miejsca";

    const examples = {
      miejsca: "kino, szpital, lotnisko, restauracja, plaża, szkoła, pociąg, teatr, statek, supermarket",
      bajki: "Kopciuszek, Królewna Śnieżka, Czerwony Kapturek, Jaś i Małgosia, Kot w butach",
      państwa: "Polska, Niemcy, Francja, Włochy, Hiszpania, Japonia, Brazylia, Egipt, Kanada, Australia"
    };

    const example = examples[query] ? `Przykłady: ${examples[query]}.` : "";

    const prompt = `Gram w grę towarzyską Spyfall. Stwórz listę 50 nazw dotyczących: ${query}. ${example} Każda nazwa powinna być po polsku, bez nazw miast (jeśli to miejsca). Oddziel każdą nazwę nową linią. Nie dodawaj żadnych komentarzy ani numeracji.`;

    const aiResponse = await env.ai.run('@cf/meta/llama-3-8b-instruct', {
      messages: [
        { role: 'system', content: 'Jesteś pomocnym asystentem generującym listy do gier towarzyskich.' },
        { role: 'user', content: prompt }
      ]
    });

    return new Response(aiResponse.response, {
      headers: { "Content-Type": "text/plain; charset=utf-8",
      "Access-Control-Allow-Origin": "*" }
    });
  }
}