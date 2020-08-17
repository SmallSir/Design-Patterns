package golang

type singleton struct{}

var instance *singleton

var mu sync.Mutex

func GetInstance() *singleton {
	if instance == nil {
		mu.Lock()
		defer mu.Unlock()
		instance = &singleton{}
	}
	return instance
}