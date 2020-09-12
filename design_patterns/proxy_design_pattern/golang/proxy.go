package proxy

type Subject interface {
	Do() string
}

type RealSubject struct {}

func (rs RealSubject) Do() string {
	return "real"
}

type Proxy struct {
	real RealSubject
}

func (p Proxy) Do() string {
	var res string

	// 调用真实对象前
	res += "pre:"

	// 调用真实对象时
	res += p.real.Do()

	// 调用真实对象后
	res += ":after"

	return res
}