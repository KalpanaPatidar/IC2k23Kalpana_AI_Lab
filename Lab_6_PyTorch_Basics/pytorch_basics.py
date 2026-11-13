try:
    import torch

    x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
    y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

    model = torch.nn.Linear(1, 1)
    loss_fn = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    for epoch in range(500):
        prediction = model(x)
        loss = loss_fn(prediction, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    with torch.no_grad():
        print("Predicted values:", model(x).flatten().tolist())
        print("Model weight:", model.weight.item())
        print("Model bias:", model.bias.item())

except ModuleNotFoundError:
    print("PyTorch is not installed in this environment.")
    print("Install it with: pip install torch")
    print("A typical linear regression workflow is: build input tensor -> model -> loss -> optimizer -> train.")
