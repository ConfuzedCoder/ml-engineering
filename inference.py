from vllm import LLM, SamplingParams

llm = LLM(model="microsoft/Phi-3-small-8k-instruct")

sampling_params = SamplingParams(temperature=0.7, top_p=0.95, max_tokens=1024)

result = llm.generate(prompt="Hello, world!", sampling_params=sampling_params)

print(result)
