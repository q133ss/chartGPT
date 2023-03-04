import openai
import keys

class Gpt:
    def gpt(self, prompt):
        openai.api_key = keys.api_key

        # задаем модель и промпт
        model_engine = "text-davinci-003"

        # задаем макс кол-во слов
        max_tokens = 128

        # генерируем ответ
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # выводим ответ
        #print(completion.choices[0].text) #ответ
        return completion.choices[0].text