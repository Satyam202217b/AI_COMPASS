def build_learning_response(
    title,
    definition,
    example,
    importance,
    bridge,
    reflection
):

    return (

        f"📘 {title}\n\n"

        f"{definition}\n\n"

        f"🔹 Example:\n{example}\n\n"

        f"⭐ Why it matters:\n{importance}\n\n"

        f"➡️ {bridge}\n\n"

        f"💭 Reflection:\n{reflection}"

    )