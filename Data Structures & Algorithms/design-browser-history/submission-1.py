class BrowserHistory:
    class ListNode:
        def __init__(self, curr, prev, next):
            self.curr = curr
            self.prev = prev
            self.next = next
    def __init__(self, homepage: str):
        self.path = self.ListNode(homepage, None, None)

    def visit(self, url: str) -> None:
        
        self.path.next = self.ListNode(url, self.path, None)
        self.path = self.path.next



    def back(self, steps: int) -> str:
        i = 0
        while self.path.prev and i < steps:
            self.path = self.path.prev
            i+=1
        return self.path.curr

    def forward(self, steps: int) -> str:
        i = 0
        while self.path.next and i < steps:
            self.path = self.path.next
            i+=1
        return self.path.curr



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)