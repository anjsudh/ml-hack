import React from 'react';


class Disease extends React.Component {

  render() {
    let bg = "linear-gradient(90deg, rgb(181, 181, 181) "+(this.props.disease[1]*100)+"%, rgb(249, 249, 249) "+((this.props.disease[1]*100)+3)+"%)"
    return (
      <li className="li disease-li" style={{background: bg}}>
          {this.props.disease[0]} {(Math.round(this.props.disease[1] * 100)) +'%'}
          <a style={{textAlign: 'center',
              float: 'right',
              cursor: 'pointer'}} onClick={()=> this.props.save(this.props.disease[0])}>✔</a>
      </li>
  );
  }

}

export default Disease;
