from server.config import *


# def classify_input(message):
#     response = client.chat.completions.create(
#         model=completion_model,
#         messages=[
#             {
#                 "role": "system",
#                 "content": """
#                         Your task is to classify if the user message is related to buildings and architecture or not.
#                         Output only the classification string.
#                         If it is related, output "Related", if not, output "Refuse to answer".

#                         # Example #
#                         User message: "How do I bake cookies?"
#                         Output: "Refuse to answer"

#                         User message: "What is the tallest skyscrapper in the world?"
#                         Output: "Related"
#                         """,
#             },
#             {
#                 "role": "user",
#                 "content": f"""
#                         {message}
#                         """,
#             },
#         ],
#     )
#     return response.choices[0].message.content


def generate_concept(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        You are a visionary intern at a leading architecture firm.
                        Your task is to craft a short, poetic, and highly imaginative concept for a building design.
                        Weave the initial information naturally into your idea, letting it inspire creative associations and unexpected imagery.
                        Your concept should feel bold, evocative, and memorable — like the opening lines of a story.
                        Keep your response to a maximum of one paragraph.
                        Avoid generic descriptions; instead, focus on mood, atmosphere, and emotional resonance.
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        What is the concept for this building? 
                        Initial information: {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content

def extract_attributes(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """

                        # Instructions #
                        You are a keyword extraction assistant.
                        Your task is to read a given text and extract relevant keywords according to three categories: shape, theme, and materials.
                        Only output a JSON object in the following format:
                        {
                            "shape": "keyword1, keyword2",
                            "theme": "keyword3, keyword4",
                            "materials": "keyword5, keyword6"
                        }

                        # Rules #
                        If a category has no relevant keywords, write "None" for that field.
                        Separate multiple keywords in the same field by commas without any additional text.
                        Do not include explanations, introductions, or any extra information—only output the JSON.
                        Focus on concise, meaningful keywords directly related to the given categories.
                        Do not try to format the json output with characters like ```json

                        # Category guidelines #
                        Shape: Words that describe form, geometry, structure (e.g., circle, rectangular, twisting, modular).
                        Theme: Words related to the overall idea, feeling, or concept (e.g., minimalism, nature, industrial, cozy).
                        Materials: Specific physical materials mentioned (e.g., wood, concrete, glass, steel).
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        # GIVEN TEXT # 
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content


def create_question(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        # Instruction #
                        You are a thoughtful research assistant specializing in architecture.
                        Your task is to create an open-ended question based on the given text.
                        Your question should invite an answer that points to references to specific brutalist buildings or notable examples.
                        Imagine the question will be answered using a detailed text about brutalist architecture.
                        The question should feel exploratory and intellectually curious.
                        Output only the question, without any extra text.

                        # Examples #
                        - What are some brutalist buildings that embody a strong relationship with the landscape?
                        - Which brutalist structures are known for their monumental scale and raw materiality?
                        - Can you name brutalist buildings that incorporate unexpected geometries or playful spatial compositions?
                        - What are examples of brutalist projects that explore the idea of community or collective living?
                        - Which architects pushed the limits of brutalist design through experimental forms?

                        # Important #
                        Keep the question open-ended, inviting multiple references or examples.
                        The question must be naturally connected to the themes present in the input text.
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content

def define_window_ratio(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        You are an international renowned architect and sustainability expert in LEED and Passive House design.
                        Your task is to provide the following suggestions based on the local climate zone or city:
                        -window to wall ratio suggestion 
                        -facade material and typical U-values
                        Keep your response to a maximum of one paragraph. Be specific and concise.
                        Provide a range of window to wall ratio (WWR) that is appropriate for the given climate zone or city.
                        Provide three facade material suggestions with typical U-values that are suitable for the local climate zone or city.
                        Avoid generic descriptions.
                        Return the answer in the following format:

                        {city}: Min {min WWR} - Max {max WWR}. 
                        Materials: 
                        {facade material 1}, 
                        {facade material 2}, 
                        {facade material 3}      
                    
                        For example:
                        "New York: Min 0.3- Max 0.5.

                        Materials: 
                        1- brick 
                        2- stone
                        3- aluminum panels
                        "
                        
                
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        what is the recommended window to wall ratio for this city for a mid rise residential building?
                        Initial information: {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content

def define_window_size(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        You are an international renowned architect and sustainability expert in passive house design.
                        Your task is to provide window dimensions in meters for a panel to a residential apartment that follows passive house design principles.
                        The window should be designed to maximize natural light and minimize heat loss.
                        The window should be designed to fit inside of a panel that is 3 meters wide and 3 meters high.
                        Provide the dimensions in meters as coordinates where [x,y] represent the bottom left corner of the window and [x,y] represent the top right corner of the window.
                        Return the answer in the following format.Do not include any other text and follow the format exactly.:
                        [x_min,y_min]
                        [x_max,y_max]
                        For example:
                        [0.5,0.5]
                        [2.5,2.5]
                        # Important #
                        Do not include any other text or explanation in the response.
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        Return the window dimensions for a mid rise residential building in the following city:
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content

def update_window(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        You are an international renowned architect and sustainability expert in passive house design.
                        Your task is to provide window dimensions in meters for a panel to a residential apartment that follows passive house design principles.
                        You will receive a message with the current window to wall ratio (WWR) and the shading depth for a specific city.
                        The window should be designed to maximize natural light and minimize heat loss.
                        Return the answer in the following format. Do not include any other text and follow the format exactly:
                        new_WWR: {new WWR}
                        new_shading_depth: {new shading depth}
                        For example:
                        new_WWR: 0.4    
                        new_shading_depth: 0.5
                        # Important #
                         
                        Provide an explanation of the new WWR and shading depth based on the local climate zone or city.
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        Return the updated new WWR and new shading depth for a mid rise residential building in the following city:
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content


def sda_analysis(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                You are an internationally renowned architect and daylighting specialist with expertise in sustainable residential design.  
                Your task is to interpret the given spatial daylight autonomy (sDA) percentage for a city given, then provide:

                1. A concise analysis of what the sDA result means for interior daylight quality.  
            
                Keep the analysis brief and focused on the implications of the sDA result in the following format, no extra text:

                analysis: {your concise analysis here}  
                                """,
                            },
                            {
                                "role": "user",
                                "content": f"""
                Here are the current metrics spatial daylight autonomy for my residential project:
                {message}
                                """,
                            },
                        ],
                    )
    return response.choices[0].message.content

def general_message(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                You are an internationally renowned architect and daylighting specialist with expertise in sustainable residential design
                Your task is to interpret the user's message as it relates to the building design and daylighting performance. Provide:
                1. A concise analysis based on the use's message.  
                2. Clear, actionable suggestions.

                Return your answer **exactly** in this format (no extra text):

                analysis: {your concise analysis here}  
                suggestions:
                - {First recommendation}
                - {Second recommendation}
                - {Third recommendation}
                                """,
                            },
                            {
                                "role": "user",
                                "content": f"""
                                {message}
                                """,
                            },
                        ],
                    )
    return response.choices[0].message.content

def classify_input(message):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
                        Your task is to classify if the user message is related to a topic question or not.
                        Output only the classification string.
                        You will receive a user message and you need to classify it as either "Relates spatial daylight autonomy (sDA)" or "Relates window to wall ratio suggestion" or "Not Related".
                        
                        # Example #
                        User message: "Here are the current metrics for my residential project: "
                        Output: "Relates spatial daylight autonomy (sDA)"

                        User message: "what is the recommended window to wall ratio for this city for a mid rise residential building?
                        Initial information:New York City"
                        Output: "Relates window to wall ratio suggestion"
                        
                        User message: "How can I improve my building design?"
                        Output: "Not Related"
                    
                        """,
            },
            {
                "role": "user",
                "content": f"""
                        {message}
                        """,
            },
        ],
    )
    return response.choices[0].message.content