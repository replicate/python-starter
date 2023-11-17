import replicate

prediction = replicate.run(
    "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
    input={
        "prompt": "a cat with a hat",
        "width": 1024,
        "height": 1024,
        "num_inference_steps": 25,
        "refine_steps": 5,
        "refine": "expert_ensemble_refiner",
    },
)

print(prediction)
