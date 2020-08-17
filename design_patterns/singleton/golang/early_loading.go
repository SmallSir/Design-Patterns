package golang


type singleton struct{

}

var instance *singleton = &singleton{}

func GetInstance() *singleton {
	return instance
}