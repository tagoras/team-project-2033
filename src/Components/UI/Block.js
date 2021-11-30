import classes from './Card.module.css';

function Block(props) {
  return <div className={classes.block}>{props.children}</div>;
}

export default Block;