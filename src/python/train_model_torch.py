import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple linear regression model
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.fc = nn.Linear(1, 1)  # Single input and output

    def forward(self, x):
        return self.fc(x)

# Generate synthetic data
X = torch.rand(100, 1)
y = 2 * X + 1 + 0.1 * torch.randn_like(X)

# Initialize and train the model
model = LinearRegressionModel()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()

# Save the trained model
torch.save(model.state_dict(), 'model.pth')
